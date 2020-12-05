import os


class Environment:
	def __init__(self):
		self.env_file = os.path.realpath('../config/env.json')

	@property
	def env_file(self):
		return self._env_file

	@env_file.setter
	def env_file(self, path_to_file):
		self._env_file = path_to_file
	pass
