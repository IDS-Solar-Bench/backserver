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

        self.client = mqttClient.Client("Python")
        self.client.username_pw_set(user, password=password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    # This function will run once we connect to the broker. We will print a message to the console.
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
        else:
            print("Connection failed")

    # This function will run every time we receive a message from the broker.
    # TODO: Message are being read as "b'message'". Need to fix this. https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
    def on_message(self, client, userdata, message):
        print("Message received: " + str(message.payload))
        self.database.addMessage(str(message.payload))

    # This function will keeping looping until we are connected to the broker.
    # Once we are connected, we will subscribe to the topic "idsbench1/measurement".
    def connect(self):

        self.client.connect(self.broker_address, port=self.port)
        self.client.loop_start()

        while not self.client.is_connected():
            time.sleep(0.1)
            
        self.client.subscribe("idsbench1/measurement")