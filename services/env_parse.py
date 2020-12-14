import json
from services.env_loader import EnvLoader
from definitions import CONFIG_PATH


class EnvParse:
	def __init__(self):
		self.data = self.get_environment_setting()

	@staticmethod
	def get_environment_setting() -> EnvLoader:
		row_data = []
		try:
			with open(CONFIG_PATH, 'r') as json_data:
				read_data: dict = json.load(json_data)
				for value in read_data.items():
					row_data.append(value)
				return EnvLoader(*row_data)
		except Exception as message:
			print(message)
		finally:
			json_data.close()
	pass
