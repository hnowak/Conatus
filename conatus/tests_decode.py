import unittest
from .decode_file import Decode


class MyTestCase(unittest.TestCase):

	def test_get_list_of_extension_data(self):
		decode = Decode('Afternoon_Ride.gpx')
		assert type(decode.get_all_track_point_data_from_gpx()) is dict


if __name__ == '__main__':
	unittest.main()
