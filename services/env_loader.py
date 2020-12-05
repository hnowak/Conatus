from dataclasses import dataclass


@dataclass
class EnvLoader:
	path_to_data: str
	db_connection: dict
	pass
