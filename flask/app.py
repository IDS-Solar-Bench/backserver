from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def fetch_message():
	try:

		# Connect to the MySQL database
		# For some reason, to get uopdated info, mysql ref must be updated every
		database = mysql.connector.connect(
			user="root",
			password="secret",
			host="mysql",
			port="3306",
			database="idsBench"
		)

		cursor = database.cursor()

		# Execute the SELECT query to retrieve data from the table
		query = "SELECT time, message FROM brokerMessage;"
		cursor.execute(query)

		# Fetch all rows from the result set
		rows = cursor.fetchall()

		# Prepare the data to be returned
		messages = [{'time': str(row[0]), 'message': row[1]} for row in rows]

		cursor.close()
		return jsonify(messages)
	except Exception as e:
		print(f"Error connecting to MySQL: {e}")
		return jsonify([])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)