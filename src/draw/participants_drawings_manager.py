import sys

sys.path.append("..")

from draw import draw
from parsers import data_parser


class ParticipantsDrawManager(object):
    def __init__(self, file_path, with_weights, draw_counter, ftype):
        self.file_obj = open(file_path)
        self.file_path = file_path
        self.with_weights = with_weights
        self.draw_counter = draw_counter
        self.ftype = ftype

    def __enter__(self):
        if self.ftype == 'json':
            if self.with_weights:
                participants = data_parser.parse_json_weighted(self.file_obj)
                drawings = draw.draw_from_json_weighted(participants, self.draw_counter)
            else:
                participants = data_parser.parse_json(self.file_obj)
                drawings = draw.draw_from_json(participants, self.draw_counter)

        elif self.ftype == 'csv':
            if self.with_weights:
                participants = data_parser.parse_csv_weighted(self.file_obj)
                drawings = draw.draw_from_csv_weighted(participants, self.draw_counter)
            else:
                participants = data_parser.parse_csv(self.file_obj)
                drawings = draw.draw_from_csv(participants, self.draw_counter)

        return drawings

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
