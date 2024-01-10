import mysql.connector

class mySqlConnector:

    def __init__(self, user, password, host, port, database):

        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

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
    def addMessage(self, message):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO brokerMessage (time, message) VALUES (CURRENT_TIMESTAMP, %s)"
        cursor.execute(insert_query, (message,))
        self.connection.commit()
        cursor.close()