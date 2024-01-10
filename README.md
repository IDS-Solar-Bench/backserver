# backserver

This repo defines four microservices run in docker.

    1. MQTT Broker
    2. Python "Funnel"
    3. MySql Database
    4. Python Flask API

IOT devices may publish messages to the broker and their data is stored in the MySql database and made avaiable at an endpoint.