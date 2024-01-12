from Classes.MQTTHandler import MQTTHandler
from Classes.mySqlConnector import mySqlConnector

import time
import os

# Get environment variables.
env = {
    "mqtt_user" : os.environ.get('MQTT_USER'),
    "mqtt_password" : os.environ.get('MQTT_PASSWORD'),
    "mysql_password" : os.environ.get('MYSQL_ROOT_PASSWORD')
}

for key in env:
    if env[key] == None:
        print("Missing environment variable: " + key)
        exit()

print("Starting funnel")

# Pass in credentials to connect to database.
database = mySqlConnector("root", env["mysql_password"], "mysql", 3306, "idsBench")

# Pass in credentials to connect to broker.
mqtt_handler = MQTTHandler("broker", 1883, env["mqtt_user"], env["mqtt_password"], database)
mqtt_handler.connect()

# Need to loop to keep the program running. Any messages from broker will be handled
# in the MQTTHandler class.
try:
    while True:
        time.sleep(1)
except SystemExit:
    print("Exiting...")
    mqtt_handler.disconnect()
    database.disconnect()
    exit()
