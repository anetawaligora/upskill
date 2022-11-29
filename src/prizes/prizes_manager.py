import sys

sys.path.append("..")

from parsers import data_parser


class PrizeManager(object):
    def __init__(self, file_path):
        self.file_obj = open(file_path)

    def __enter__(self):
        parsed_json = data_parser.parse_json(self.file_obj)

        return parsed_json['prizes']

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
