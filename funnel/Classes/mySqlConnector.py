import mysql.connector

class mySqlConnector:


    def __init__(self, user: str, password: str, host: str, port: int, database: str):

        # Connect to the MySql database using the credentials passed in.
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        # We do not know if this is the first time we are connecting to the database.
        # In the case that we are, we must pass these SQL commands to create the database and table.
        # In the case that we are not, these commands will not do anything.
        # TODO: Need to create a table with temp and capacity columns.
        sql_commands = [
            "CREATE DATABASE IF NOT EXISTS idsBench;",
            "USE idsBench;",
            "CREATE TABLE IF NOT EXISTS brokerMessage (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, message TEXT NOT NULL);"
        ]

        for command in sql_commands:
            cursor = self.connection.cursor()
            cursor.execute(command)
            self.connection.commit()
            cursor.close()

    
    # Adding a message from broker into database.
    # TODO: The message we need from the broker is actually two different values temp and capcity.
    #       Need to decide how to break this data up. Whether this is in one message like "temp,capcity"
    #       or we send through different topics like "idsbench1/temp" and "idsbench1/capcity
    def addMessage(self, message):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO brokerMessage (time, message) VALUES (CURRENT_TIMESTAMP, %s)"
        cursor.execute(insert_query, (message,))
        self.connection.commit()
        cursor.close()