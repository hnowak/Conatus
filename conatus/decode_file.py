import os
from typing import *
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from extension_data import ExtensionData


class Decode:
	def __init__(self, file_name: str):
		if not os.path.exists(os.path.join('import', file_name)):
			print(os.path.join('../import', file_name))
			raise FileNotFoundError
		else:
			self.file_name = os.path.join('../import', file_name)

	@property
	def file_name(self):
		return self._file_name

	@file_name.setter
	def file_name(self, value):
		self._file_name = value

	@file_name.deleter
	def file_name(self):
		"""
		This property remove the file which exist in object instance and remove the instance.
		"""
		if not os.path.exists(self._file_name):
			raise FileNotFoundError
		else:
			os.remove(self._file_name)
			print('File deleted')
			del self

	def __del__(self):
		print("Reference to object was destroy!")

	def _find_namespace(self) -> dict:
		"""
		Function found all of namespaces in XML file
		:return: Dictionary for ElementTree object (user for find(), findall()
		"""
		return dict(node for _, node in ElementTree.iterparse(self._file_name, events=['start-ns']))

	def get_all_track_point_data_by_tag(self, search_xpath: str) -> List[Element]:
		"""
		This function takes an XPATH argument and returns a list of Element objects.
		:param search_xpath: 'str'
		:return: List[Element]
		"""
		return ElementTree.parse(self._file_name).getroot().findall(search_xpath, self._find_namespace())

	def do_iter(self):
		ns = self._find_namespace()
		track_point_list = ElementTree.iterparse(self._file_name, ns)
		for t in iter(track_point_list):
			print(t)

	def get_all_track_point_data_from_gpx(self):
		# todo Create info
		ns = self._find_namespace()
		track_point_list: List[Element] = ElementTree.parse(self._file_name).getroot().findall('trk/trkseg//', ns)

		test_dict = {}
		data = []
		count = 0

		for tp in track_point_list:
			if 'trkpt' in tp.tag.split('}')[1]:
				count += 1
				data.append(tp.attrib)
				for extensions in tp.findall("./", ns):
					data.append(extensions.text) if len(
						extensions.text) > 0 and not extensions.text.isspace() else False
					for dt in extensions.findall("*/", ns):
						data.append(dt.text)
				test_dict[count] = ExtensionData(*data)
				data = []
		return test_dict
	pass
