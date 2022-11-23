import data_parser as parser


class PrizeManager(object):
    def __init__(self, file_path):
        self.file_obj = open(file_path)

    def __enter__(self):
        parsed_json = parser.parse_json(self.file_obj)

        return parsed_json['prizes']

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
