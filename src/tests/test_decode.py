import unittest
from conatus.decode_file import Decode


class MyTestCase(unittest.TestCase):

	def test_get_list_of_extension_data(self):
		decode = Decode('Afternoon_Ride.gpx')
		list_of_data = decode.get_all_track_point_data_from_gpx()
		# print(list_of_data)
		assert type(list_of_data) is dict


if __name__ == '__main__':
	unittest.main()
