import json
import sys
from pathlib import Path

sys.path.append("..")


class PrizeManager(object):
    def __init__(self, file_path):
        self.file_obj = open(PrizeManager.get_separate_prizes_template(file_path))

    def __enter__(self):
        parsed_json = json.load(self.file_obj)

        return parsed_json['prizes']

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    @staticmethod
    def get_separate_prizes_template(template_file):
        lottery_templates_directory = Path.joinpath(Path().absolute(), 'src/data/lottery_templates')

        if template_file:
            return Path.joinpath(lottery_templates_directory, template_file)

        return Path.joinpath(lottery_templates_directory,
                             PrizeManager.get_first_prize_template(lottery_templates_directory))

    @staticmethod
    def get_first_prize_template(directory):
        return sorted(list(directory.iterdir()))[0]
