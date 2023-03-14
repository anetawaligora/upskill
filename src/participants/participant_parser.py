import csv
import json
import sys
from typing import List

sys.path.append("..")

from participants.participant import Participant


class ParticipantParser(object):
    def __init__(self, file_path, with_weights, ftype):
        self.file_obj = open(file_path)
        self.file_path = file_path
        self.with_weights = with_weights
        self.ftype = ftype

    def __enter__(self):
        if self.ftype == 'json':
            participants = ParticipantParser.parse_json(self.file_obj, self.with_weights)

        elif self.ftype == 'csv':
            participants = ParticipantParser.parse_csv(self.file_obj, self.with_weights)

        return participants

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    @staticmethod
    def parse_json(file, with_weights=False) -> List[Participant]:
        participants = list()
        for item in json.load(file):
            if isinstance(item, dict):
                participant = Participant(item['id'], item['first_name'], item['last_name'],
                                          item['weight']) if with_weights else Participant(item['id'],
                                                                                           item['first_name'],
                                                                                           item['last_name'],
                                                                                           item['weight'])
                participants.append(participant)

        return participants

    @staticmethod
    def parse_csv(file, with_weights) -> List[Participant]:
        participants_reader = csv.reader(file, delimiter=',', quotechar='|')
        participants = list()
        for item in list(participants_reader)[1:]:
            participant = Participant(item[0], item[1], item[2],
                                      item[3]) if with_weights else Participant(item[0], item[1], item[2])
            participants.append(participant)

        return participants
