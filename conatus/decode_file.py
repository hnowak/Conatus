import os
from typing import *
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from .extension_data import ExtensionData


class Decode:
	_PATH_TO_DATA = os.path.join(os.path.realpath(os.curdir), 'data')

	def __init__(self, file_name: str):
		if not os.path.exists(os.path.join('data', file_name)):
			print('test')
			raise FileNotFoundError
		else:
			self.file_name = os.path.join('data', file_name)

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
		return ElementTree.parse(self._file_name).getroot().findall(search_xpath, self._find_namespace())

	def do_iter(self):
		ns = self._find_namespace()
		track_point_list = ElementTree.iterparse(self._file_name, ns)
		for t in iter(track_point_list):
			print(t)
		# ElementTree.dump(ElementTree.parse(self._file_name))

	def get_all_track_point_data_from_gpx(self):
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
					data.append(extensions.text) if len(extensions.text) > 0 and not extensions.text.isspace() else False
					for dt in extensions.findall("*/", ns):
						data.append(dt.text)
				test_dict[count] = ExtensionData(*data)
				data = []
		return test_dict


if __name__ == "__main__":
	pass
	# todo function to collect the data from XML base on collection given by enym?


# def _take_files_from_dir(self) -> List[str]:
#     return [file for file in os.listdir(self._path_to_data)]

# def json_test(self):
#     for file_name in self._take_files_from_dir():
#         file = os.path.join(self._path_to_data, file_name)
#         with open(file, 'r') as json_file:
#             data = json.load(json_file)
#             data_from_json = json.dumps(data["data"][0]['values'])
#             print(data_from_json)

# def loop_data(self):
#     mytree = ElementTree.parse('data/file.gpx')
#     myroot = mytree.getroot()
#
#     my_namespaces = dict(
#         node for _, node in ElementTree.iterparse('data/file.gpx', events=['start-ns'])
#     )
#
#     track_point_list: List[Element] = myroot.findall('trk/trkseg//', my_namespaces)
#     # track_points_extension_list: List[Element] = myroot.findall(".//gpxtpx:TrackPointExtension//", my_namespaces)
#
#     test_dict = {}
#     point = None
#     data = []
#
#     count = 0
#     for tp in track_point_list:
#         if 'trkpt' in tp.tag.split('}')[1]:
#             # print()
#             # print('Pick: ', count)
#             # print(tp.attrib)
#             count += 1
#             point = tp.attrib
#             data.append(point)
#             for extensions in tp.findall("./", my_namespaces):
#                 data.append(extensions.text) if len(
#                     extensions.text) > 0 and not extensions.text.isspace() else False
#                 for dt in extensions.findall("*/", my_namespaces):
#                     data.append(dt.text)
#             test_dict[count] = data
#             data = []
#         else:
#             False
#         # todo: resolve problem with get the elevation and time data
#         # print(tp.tag.split('}')[1], tp.text) if len(tp.text) > 0 and not tp.text.isspace() else False
#
#     for k, v in test_dict.items():
#         print(k, v)