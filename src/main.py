# python mvp.pyFILES = {}
# load the contents of files into FILES should_draw = Truewhile should_draw:
# question - from which file to lottery
# question - if there are weights in the file
# question - how many times to make a lottery
# Winners drawing
# Print the list of winners
# question - whether to continue lottery or end the program
# if continue to lottery --> choose a file and repeat steps , if end program print "End of drawing"

import click

from participants.participant_draw_manager import ParticipantDrawManager
from interface import interface
from participants.participant_parser import ParticipantParser
from prizes.prizes_manager import PrizeManager
from utils import file_utils
from lottery.lottery import Lottery


@click.command()
@click.argument('participants')
@click.option('--weights', '-w', default=False, type=click.BOOL, help='File contains weight')
@click.option('--ftype', '-f', default='json', type=click.Choice(['json', 'csv']),
              help='The format of participants file')
@click.option('--times', '-t', default=1, help='Times of drawing')
@click.option('--lottery_template', '-lt', help='The lottery template')
@click.option('--output', '-o', type=click.File('w'), help='The output file')
def parse_command(participants, weights, ftype, times, lottery_template, output):
    results = draw(participants, weights, ftype, times, lottery_template)

    if output:
        output.write(file_utils.as_json(results))
    else:
        interface.show_winners(results)


def draw(participants_file, with_weights, ftype, draw_counter, lottery_template):
    file_path = file_utils.get_participants_file_path(participants_file)

    with ParticipantParser(file_path, with_weights, ftype) as participants, PrizeManager(
            lottery_template) as prizes:
        drown_participants = ParticipantDrawManager.draw(participants, draw_counter, with_weights)
        return Lottery.get_winners(drown_participants, prizes)


if __name__ == '__main__':
    parse_command()
