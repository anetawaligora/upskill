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
        return self.parse()

    def parse(self):
        participants = []
        if self.ftype == 'json':
            participants = self.parse_json()

        elif self.ftype == 'csv':
            participants = self.parse_csv()

        return participants

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def parse_json(self) -> List[Participant]:
        participants = list()
        for item in json.load(self.file_obj):
            if isinstance(item, dict):
                participant = Participant(item['id'], item['first_name'], item['last_name'],
                                          item['weight']) if self.with_weights else Participant(item['id'],
                                                                                                item['first_name'],
                                                                                                item['last_name'],
                                                                                                item['weight'])
                participants.append(participant)

        return participants

    def parse_csv(self) -> List[Participant]:
        participants_reader = csv.reader(self.file_obj, delimiter=',', quotechar='|')
        participants = list()
        for item in list(participants_reader)[1:]:
            participant = Participant(item[0], item[1], item[2],
                                      item[3]) if self.with_weights else Participant(item[0], item[1], item[2])
            participants.append(participant)

        return participants
