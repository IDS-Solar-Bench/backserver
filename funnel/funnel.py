from Classes.MQTTHandler import MQTTHandler
from Classes.mySqlConnector import mySqlConnector

import time


print("Starting funnel")

# Pass in credentials to connect to database.
database = mySqlConnector("root", "secret", "mysql", "3306", "idsBench")

# Pass in credentials to connect to broker.
broker_address = 'broker'
port = 1883
user = "sam"
password = "idssolarbench"

mqtt_handler = MQTTHandler(broker_address, port, user, password, database)
mqtt_handler.connect()

# Need to loop to keep the program running. Any messages from broker will be handled
# in the MQTTHandler class.
while True:
    time.sleep(1)