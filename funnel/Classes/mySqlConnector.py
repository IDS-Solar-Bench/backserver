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