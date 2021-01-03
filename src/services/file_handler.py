import os
import re
from typing import AnyStr, List, Optional

from src.definitions import IMPORT_PATH


class FileHandler:
    def __init__(self):
        self.list_of_file = []

    def get_specific_file_from_folder(self, filename: AnyStr = None, file_format: Optional = None) -> AnyStr:
        if filename is None:
            raise ValueError
        for fn in os.listdir(IMPORT_PATH):
            fn = fn.split('.')[0]
            if fn == filename.split(".")[0]:
                print("Found")

    # TODO How found file with multiple dots in file name?? (remove dots or split)

    def set_list_by_file_in_folder(self) -> List[AnyStr]:
        pass

    @classmethod
    def is_json(cls, filename: AnyStr) -> bool:
        try:
            with open(os.path.join(IMPORT_PATH, filename), 'r') as unknown_file:
                data = re.sub(r'\s+', '', unknown_file.read())
                if re.match(r'^({|[).+(}|])$', data):
                    unknown_file.close()
                    return True
                return False
        except Exception as message:
            print(message)

    @classmethod
    def is_xml(cls, filename: AnyStr) -> bool:
        try:
            with open(os.path.join(IMPORT_PATH, filename), 'r') as unknown_file:
                data = re.sub(r'\s+', '', unknown_file.read())
                if re.match(r'^<.+>$', data):
                    unknown_file.close()
                    return True
                return False
        except Exception as message:
            print(message)


if __name__ == "__main__":
    # print(FileHandler.is_xml("Afternoon_Ride.gpx"))
    f = FileHandler()
    f.get_specific_file_from_folder("Afternoon_Ride.gpx")
