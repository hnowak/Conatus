import mysql.connector
from mysql.connector import errorcode

from services.env_parse import EnvParse


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
		finally:
			conn.close()

	def query_handler(self, sql_query: str, *args, **kwargs):
		connection = self.connect()
		# connection.cursor()
		connection.close()

	pass
