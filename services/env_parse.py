import json
from services.env_loader import EnvLoader
from services.envionment import Environment


class EnvParse(Environment):
	def __init__(self):
		super().__init__()

	def get_environment_setting(self) -> EnvLoader:
		row_data = []
		try:
			with open(self._env_file, 'r') as json_data:
				read_data: dict = json.load(json_data)
				for key, value in read_data.items():
					row_data.append(value)
				return EnvLoader(*row_data)
		except Exception as message:
			print(message)
		finally:
			json_data.close()


if __name__ == "__main__":
	e = EnvParse()
	print(e.get_environment_setting())
	pass
