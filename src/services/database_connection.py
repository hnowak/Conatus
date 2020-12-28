import mysql.connector
from mysql.connector import errorcode

from src.services import EnvParse


class Connection:
	def __init__(self):
		self.data_to_connect = EnvParse().data.db_connection

	def connect(self) -> mysql.connector.MySQLConnection:
		conn = None
		try:
			conn = mysql.connector.connect(**self.data_to_connect)
			return conn
		except mysql.connector.Error as error:
			if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif error.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(error)
				conn.close()

	def query_select_handler(self, sql_query: str) -> list:
		connection = self.connect()
		cursor = connection.cursor()
		try:
			cursor.execute(sql_query)
			return cursor.fetchall()
		except mysql.connector.Error as error:
			print(error)
		finally:
			cursor.close()
			connection.close()

	def query_insert_file_row_into_db(self, value_params: list):
		connection = self.connect()
		cursor = connection.cursor()
		try:
			query = f"INSERT INTO conatus.xml_data(track_id, point, elevation, temperature, heart_rate, cadence, time) VALUES {*value_params,};"
			cursor.execute(query)
			connection.commit()
		except mysql.connector.Error as error:
			print(error)
		finally:
			cursor.close()
			connection.close()
	pass
