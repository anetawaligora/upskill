from pathlib import Path


def get_separate_prizes_template():
    lottery_templates_directory = Path.joinpath(Path().absolute(), 'data/lottery_templates')
    return Path.joinpath(lottery_templates_directory, 'separate_prizes.json')
