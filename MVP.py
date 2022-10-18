# python mvp.pyFILES = {}
# load the contents of files into FILES should_draw = Truewhile should_draw:
# question - from which file to draw
# question - if there are weights in the file
# question - how many times to make a draw
# Winners drawing
# Print the list of winners
# question - whether to continue draw or end the program
# if continue to draw --> choose a file and repeat steps , if end program print "End of drawing"

import csv
import random
import json
import os


def draw_from_json(file, draw_counter):
    participants = json.load(file)
    return random.choices(participants, k=draw_counter)


def draw_from_json_weighted(file, draw_counter):
    participants = json.load(file)
    participants = list(participants)
    weights = [int(participant['weight']) for participant in participants]
    return random.choices(participants, k=draw_counter, weights=weights)


def draw_from_csv(file, draw_counter):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    participants = list(participants_reader)[1:]
    return random.choices(participants, k=draw_counter)


def draw_from_csv_weighted(file, draw_counter):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    participants = list(participants_reader)[1:]
    weights = [int(participant[3]) for participant in participants]
    return random.choices(participants, k=draw_counter, weights=weights)


def show_available_input_files():
    root_folder = os.getcwd()
    data_folder = root_folder + '\data\inputs'
    print('Available files: ' + ' '.join(os.listdir(data_folder)))


def draw():
    show_available_input_files()
    input_files_directory = os.getcwd() + '\data\inputs'
    filename = input("Please provide filename with data:")
    with_weights = input("Do exist weights in loaded file? y/n")
    draw_counter = int(input("How many times to make a draw?"))

    file_path = os.path.join(input_files_directory, filename)
    print(file_path)

    with open(file_path) as file:
        if file_path.endswith('.json'):
            if with_weights == 'y':
                drawings = draw_from_json_weighted(file, draw_counter)
            else:
                drawings = draw_from_json(file, draw_counter)
        elif file_path.endswith('.csv'):
            if with_weights == 'y':
                drawings = draw_from_csv_weighted(file, draw_counter)
            else:
                drawings = draw_from_csv(file, draw_counter)

        file.close()

    print(drawings)


choice = "YES"

while choice.upper() == "YES":
    draw()
    choice = input("Do you want to continue to draw winners? Answer Yes or No ")

print("End of drawing")
exit(0)
