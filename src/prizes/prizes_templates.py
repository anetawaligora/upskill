from pathlib import Path


def get_separate_prizes_template(template_file):
    lottery_templates_directory = Path.joinpath(Path().absolute(), 'src/data/lottery_templates')

    if template_file:
        return Path.joinpath(lottery_templates_directory, template_file)

    return Path.joinpath(lottery_templates_directory, get_first_prize_template(lottery_templates_directory))


def get_first_prize_template(directory):
    return sorted(list(directory.iterdir()))[0]
