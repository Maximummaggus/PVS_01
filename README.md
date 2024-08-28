TEKO Olten: Parallele und verteilte Systeme
Leistungsbeurteilung PVS-01

Diese Arbeit umfasst folgenden Auftrag:
Entwickeln Sie ein verteiltes Finanzsystem welches fiktive Finanzdaten verarbeitet und diese entsprechend abspeichert.
Der Producer welcher synthetische Finanzdaten erzeugt ist als Source Code vorhanden und muss in einen Docker
Container verpackt werden. Weiter sendet er die Daten in ein Message Broker System «RabbitMQ» in verschiedene
Queues um diese dort für die weitere Verarbeitung zwischenzuspeichern. Die Consumer sollen nur jeweils eine
bestimmte Gruppe von Finanzdaten verarbeiten und diese sollen aus einer spezifischen RabbitMQ Queue gelesen
werden. Die Consumer sollen jeweils in 1000er Paketen Daten lesen und daraus den Durchschnitt berechnen und dieses
Resultat danach in eine MongoDB speichern. Die MongoDB soll als Cluster Verbund aufgebaut sein (als Replicaset) sodass
eine Ausfallsicherheit gewährleistet werden kann. Weiter sollen die aggregierten Finanzdaten über ein «Frontend»
einsehbar sein welches auch als Source Code zur Verfügung gestellt wird und in einen Docker Container verpackt werden
soll. Auch das Frontend soll ausfallsicher gestaltet werden und soll daher aus mindestens 2 Instanzen bestehen mit einem
Load Balancer, der die Anfragen auf die Systeme verteilt.
![image](https://github.com/user-attachments/assets/f703f78c-9b1d-4e99-8c7a-d5bfc3f9485f)


Wichtig:
vor dem Ausführen alle Container, Images und Volumes im Docker Desktop löschen
