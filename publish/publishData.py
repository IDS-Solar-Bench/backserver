import paho.mqtt.client as paho
import random 
import time

broker_address= "localhost"
port = 1883
user = "user"
password = "perwana"

def on_publish(client,userdata,result):             #create function for callback
    print(result)
    pass

client1= paho.Client("control1")                           #create client object
client1.username_pw_set(user, password=password)    #set username and password
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker_address, port)                           #establish connection



while True:
    time.sleep(5)
    temp = round(random.uniform(0,100), 1)
    capacity = int(random.uniform(0,100))
    message = "Hello, World!"

    payload = str(temp) + "," + str(capacity) + "," + message
    print(payload)

    ret= client1.publish("idsbench1/measurement", payload)