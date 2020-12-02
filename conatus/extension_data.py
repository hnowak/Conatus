from dataclasses import dataclass


@dataclass
class ExtensionData:
	trkpt: dict
	ele: float
	time: str
	atemp: int
	hr: int
	cad: int
	pass
