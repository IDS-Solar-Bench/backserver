import paho.mqtt.client as mqttClient
from Classes.mySqlConnector import mySqlConnector
import time

# This class hides logic of connecting to broker and adding messages into database.

class MQTTHandler:

    # In our init step, we connect to the broker using our credentials pass in.
    # We also set up our callbacks for when we connect to the broker and when we receive a message.
    def __init__(self, broker_address: str, port: int, user: str, password: str, database: mySqlConnector) -> None:

        self.database = database
        self.broker_address = broker_address
        self.port = port
        self.user = user
        self.password = password

        self.client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
        self.client.username_pw_set(user, password=password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    # This function will run once we connect to the broker. We will print a message to the console.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
        else:
            print("Connection failed")

    def on_message(self, client, userdata, message):

        message_decode = str(message.payload.decode("utf-8"))
        message_split = message_decode.split(",")

        print("Message received: Temperature: " + message_split[0] + " Capacity: " + message_split[1] + " Message: " + message_split[2])        

        self.database.addMessage(message_split[0], message_split[1], message_split[2])

    # This function will keeping looping until we are connected to the broker.
    # Once we are connected, we will subscribe to the topic "idsbench1/measurement".
    def connect(self):

        self.client.connect(self.broker_address, port=self.port)
        self.client.loop_start()

        while not self.client.is_connected():
            time.sleep(0.1)
            
        self.client.subscribe("idsbench1/measurement")
    
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()