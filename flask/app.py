from flask import Flask, jsonify
import mysql.connector
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

scheduler = BackgroundScheduler()

datafromSql = []

# We do not want to be calling from the database every time we get an API call
def update():

	# Connect to the MySQL database
	# For some reason, to get updated info, mysql ref must be updated every time
	database = None

	try:
		database = mysql.connector.connect(
			user="root",
			password="secret",
			host="mysql",
			port="3306",
			database="idsBench"
		)
	# If the connection fails, try again
	except (mysql.connector.errors.InterfaceError):
		print("MySQL connection error. Trying again.")
		return

	cursor = database.cursor()

	# Execute the SELECT query to retrieve data from the table
	query = "SELECT time, temperature, capacity, message FROM brokerMessage;"
	cursor.execute(query)

	# Fetch all rows from the result set
	rows = cursor.fetchall()

	# Prepare the data to be returned
	messages = [{'time': str(row[0]), 'temp' : float(row[1]), 'capacity' : int(row[2]), 'message': row[1]} for row in rows]

	cursor.close()

	global datafromSql
	datafromSql = messages

	return


scheduler.add_job(update, 'interval', seconds=5)
scheduler.start()

@app.route('/')
def fetch_message():
	return jsonify(datafromSql)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)