import json
import sys
from pathlib import Path
from typing import List

sys.path.append("..")

from prizes.prize import Prize


class PrizeParser(object):
    def __init__(self, file_path, templates_directory):
        self.templates_directory = templates_directory
        self.file_obj = open(self.get_separate_prizes_template(file_path))

    def __enter__(self):
        return self.parse()

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def parse(self) -> List[Prize]:
        parsed_json = json.load(self.file_obj)
        prizes = []

        for item in parsed_json['prizes']:
            prize = Prize(item['id'], item['name'])
            for prizeIndex in range(int(item['amount'])):
                prizes.append(prize)

        return prizes

    def get_separate_prizes_template(self, template_file):
        lottery_templates_directory = Path.joinpath(Path().absolute(), self.templates_directory)

        if template_file:
            return Path.joinpath(lottery_templates_directory, template_file)

        return Path.joinpath(lottery_templates_directory,
                             PrizeParser.get_first_prize_template(lottery_templates_directory))

    @staticmethod
    def get_first_prize_template(directory):
        return sorted(list(directory.iterdir()))[0]
