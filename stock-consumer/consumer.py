import os
import pika
import json
from pymongo import MongoClient


def get_rabbitmq_connection():
    rabbitmq_url = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    params = pika.URLParameters(rabbitmq_url)
    connection = pika.BlockingConnection(params)
    return connection

def get_mongodb_connection():
    mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
    client = MongoClient(mongodb_url)
    return client

def process_messages(channel, method, properties, body):
    data = json.loads(body)
    print(f"Received message: {data}")

    # Nachrichten zwischenspeichern
    global buffer
    buffer.append(data)

    if len(buffer) >= 1000:
        avg_price = sum(item['price'] for item in buffer) / len(buffer)
        company = buffer[0]['company']

        # Daten in MongoDB speichern
        db = mongodb_client['stockmarket']
        collection = db['stocks']
        collection.update_one(
            {'company': company},
            {'$set': {'company': company, 'avgPrice': avg_price}},
            upsert=True
        )
        print(f"Inserted/Updated avgPrice for {company}: {avg_price}")
        buffer.clear()

    # Nachrichten bestätigen
    channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    queue_name = os.getenv("QUEUE_NAME", "default_queue")

    # Verbindung zu RabbitMQ herstellen
    rabbitmq_connection = get_rabbitmq_connection()
    channel = rabbitmq_connection.channel()

    # Verbindung zu MongoDB herstellen
    mongodb_client = get_mongodb_connection()

    buffer = []

    # Die Queue abonnieren
    channel.basic_consume(queue=queue_name, on_message_callback=process_messages, auto_ack=False)

    print(f" [*] Waiting for messages in {queue_name}. To exit press CTRL+C")
    channel.start_consuming()
