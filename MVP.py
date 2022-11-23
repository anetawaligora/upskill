# python mvp.pyFILES = {}
# load the contents of files into FILES should_draw = Truewhile should_draw:
# question - from which file to draw
# question - if there are weights in the file
# question - how many times to make a draw
# Winners drawing
# Print the list of winners
# question - whether to continue draw or end the program
# if continue to draw --> choose a file and repeat steps , if end program print "End of drawing"

import interface
from lottery_templates import get_separate_prizes_template
from participants_drawings_manager import ParticipantsDrawManager
from prize_manager import PrizeManager


def draw():
    p = get_separate_prizes_template()
    print(p)
    file_path, with_weights, draw_counter = interface.initialize_drawings()
    with ParticipantsDrawManager(file_path, with_weights, draw_counter) as drawings, PrizeManager(
            get_separate_prizes_template()) as prizes:
        interface.show_winners(drawings, file_path, prizes)


if __name__ == '__main__':
    choice = "YES"

    while choice.upper() == "YES":
        draw()
        choice = input("Do you want to continue to draw winners? Answer Yes or No ")

    print("End of drawing")
    exit(0)
