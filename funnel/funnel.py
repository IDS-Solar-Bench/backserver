from Classes.MQTTHandler import MQTTHandler
from Classes.mySqlConnector import mySqlConnector

import time

print("Starting funnel")

database = mySqlConnector("root", "secret", "mysql", "3306", "idsBench")

broker_address = 'broker'
port = 1883
user = "sam"
password = "idssolarbench"

mqtt_handler = MQTTHandler(broker_address, port, user, password, database)
mqtt_handler.connect()

while True:
    time.sleep(1)