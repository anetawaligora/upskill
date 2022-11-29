# python mvp.pyFILES = {}
# load the contents of files into FILES should_draw = Truewhile should_draw:
# question - from which file to draw
# question - if there are weights in the file
# question - how many times to make a draw
# Winners drawing
# Print the list of winners
# question - whether to continue draw or end the program
# if continue to draw --> choose a file and repeat steps , if end program print "End of drawing"


from draw import participants_drawings_manager
from interface import interface
from prizes import prizes_manager, prizes_templates


def draw():
    file_path, with_weights, draw_counter = interface.initialize_drawings()
    with participants_drawings_manager.ParticipantsDrawManager(file_path, with_weights,
                                                               draw_counter) as drawings, prizes_manager.PrizeManager(
        prizes_templates.get_separate_prizes_template()) as prizes:
        interface.show_winners(drawings, file_path, prizes)


if __name__ == '__main__':
    choice = "YES"

    while choice.upper() == "YES":
        draw()
        choice = input("Do you want to continue to draw winners? Answer Yes or No ")

    print("End of drawing")
    exit(0)
