# IDS Solar Bench Backserver

This repo defines four microservices.

    1. MQTT Broker
    2. Python "Funnel"
    3. MySql Database
    4. Python Flask API

On a broad scale, the purpose of these microservices is to store and make JSON readable measurements from IOT devices. 

Data travels through these microservices as follows...

## Eclipse Mosquitto Broker

The bench microcontroller will publish messages to the broker containing the temp and capacity of the battery to the topic "idsbench1/measurement". The broker will then pass that measurement to all programs subscribed to the topic.

## Python "Funnel"

The funnel is a constantly running Python project that is subscribed to the topic "idsbench1/measurement" on the broker. When a message is sent through the broker, the funnel will receive and "funnel" the message into the MySql server.

## MySql

Stores the measurements from the microcontroller on database "idsBench" on one table (If the number of benches expands, there is a possibility to expand the number of tables in the database). This table holds cols "Time", "Temp", "Capacity." Importantly, MySql data is tied to a docker volume and therefore the data will persist between containers.

## Flask

Lastly, the Flask app allows retival from the MySql database through REST API in JSON format. It will update it's data every XXXX seconds.
