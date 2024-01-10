import paho.mqtt.client as mqttClient
import mysql.connector
import time

class MQTTHandler:

    def __init__(self, broker_address, port, user, password, database) -> None:

        self.database = database
        self.broker_address = broker_address
        self.port = port
        self.user = user
        self.password = password

        self.client = mqttClient.Client("Python")               #create new instance
        self.client.username_pw_set(user, password=password)    #set username and password

        self.client.on_connect = self.on_connect                      #attach function to callback
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
        else:
            print("Connection failed")

    def on_message(self, client, userdata, message):
        print("Message received: " + str(message.payload))
        self.database.addMessage(str(message.payload))

    def connect(self):

        self.client.connect(self.broker_address, port=self.port)
        self.client.loop_start()

        while not self.client.is_connected():
            time.sleep(0.1)
            
        self.client.subscribe("python/test")

class database:

    def __init__(self, user, password, host, port, database):

        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
    
    # Adding a message from broker into database.
    def addMessage(self, message):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO brokerMessage (time, message) VALUES (CURRENT_TIMESTAMP, %s)"
        cursor.execute(insert_query, (message,))
        self.connection.commit()
        cursor.close()