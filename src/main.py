# python mvp.pyFILES = {}
# load the contents of files into FILES should_draw = Truewhile should_draw:
# question - from which file to draw
# question - if there are weights in the file
# question - how many times to make a draw
# Winners drawing
# Print the list of winners
# question - whether to continue draw or end the program
# if continue to draw --> choose a file and repeat steps , if end program print "End of drawing"

import click

from draw import participants_drawings_manager
from interface import interface
from prizes import prizes_manager, prizes_templates
from utils import file_utils


@click.command()
@click.argument('participants')
@click.option('--weights', '-w', default=False, type=click.BOOL, help='File contains weight')
@click.option('--ftype', '-f', default='json', type=click.Choice(['json', 'csv']),
              help='The format of participants file')
@click.option('--times', '-t', default=1, help='Times of drawing')
@click.option('--lottery_template', '-lt', help='The lottery template')
@click.option('--output', '-o', help='The output file')
def parse_command(participants, weights, ftype, times, lottery_template, output):
    draw(participants, weights, ftype, times, lottery_template)


def draw(participants_file, with_weights, ftype, draw_counter, lottery_template):
    file_path = file_utils.get_participants_file_path(participants_file)

    with participants_drawings_manager.ParticipantsDrawManager(file_path, with_weights,
                                                               draw_counter,
                                                               ftype) as drawings, prizes_manager.PrizeManager(
        prizes_templates.get_separate_prizes_template(lottery_template)) as prizes:
        interface.show_winners(drawings, file_path, prizes)


if __name__ == '__main__':
    parse_command()
