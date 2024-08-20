import os
import pika
import pymongo
import json
from statistics import mean
from datetime import datetime

rabbitmq_url = os.getenv('RABBITMQ_URL')
mongodb_url = os.getenv('MONGODB_URL')
queue_name = os.getenv('QUEUE_NAME')

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)
db = client['stockdb']
collection = db['average_prices']

# Connect to RabbitMQ

