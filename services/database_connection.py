import mysql.connector
from services.env_parse import EnvParse


class Connection:
	def __init__(self):
		self.connection = mysql.connector.connect(**EnvParse().get_environment_setting().db_connection)
	pass





