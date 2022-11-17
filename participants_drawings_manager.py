import draw
import data_parser as parser


class ParticipantsDrawManager(object):
    def __init__(self, file_path, with_weights, draw_counter):
        self.file_obj = open(file_path)
        self.file_path = file_path
        self.with_weights = with_weights
        self.draw_counter = draw_counter

    def __enter__(self):
        if self.file_path.name.endswith('.json'):
            if self.with_weights == 'y':
                participants = parser.parse_json_weighted(self.file_obj)
                drawings = draw.draw_from_json_weighted(participants, self.draw_counter)
            else:
                participants = parser.parse_json(self.file_obj)
                drawings = draw.draw_from_json(participants, self.draw_counter)

        elif self.file_path.name.endswith('.csv'):
            if self.with_weights == 'y':
                participants = parser.parse_csv_weighted(self.file_obj)
                drawings = draw.draw_from_csv_weighted(participants, self.draw_counter)
            else:
                participants = parser.parse_csv(self.file_obj)
                drawings = draw.draw_from_csv(participants, self.draw_counter)

        return drawings

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
