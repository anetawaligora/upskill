# python mvp.pyFILES = {}
# wczytać zawartość plików do FILES should_draw = Truewhile should_draw:
# pytanie - czy losować czy zakończyć program
# pytanie - ilu zwycięzców
# pytanie - który plik użyć (wyświetlić listę plików <opcje>)
# użytkowenik wybiera plik, w zależności od tego używamy funkcji losującej
# losowanie wygranych
# wyświtlić zwycięzców

import csv
import random
import json


def draw_from_json(file, draw_counter):
    participants = json.load(file)
    return random.choices(participants, k=draw_counter)


def draw_from_json_weighted(file, draw_counter):
    return None


def draw_from_csv(file, draw_counter):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    participants = list(participants_reader)[1:]
    return random.choices(participants, k=draw_counter)


def draw_from_csv_weighted(file, draw_counter):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    participants = list(participants_reader)[1:]
    weights = [int(participant[3]) for participant in participants]
    return random.choices(participants, k=draw_counter, weights=weights)


def draw():
    filename = input("Please provide filename with data:")
    with_weights = input("Do exist weights in loaded file? y/n")
    draw_counter = int(input("How many times to make a draw?"))

    with open(filename) as file:
        if filename.endswith('.json'):
            if with_weights == 'y':
                drawings = draw_from_json_weighted(file, draw_counter)
            else:
                drawings = draw_from_json(file, draw_counter)
        elif filename.endswith('.csv'):
            if with_weights == 'y':
                drawings = draw_from_csv(file, draw_counter)
            else:
                drawings = draw_from_csv_weighted(file, draw_counter)

        file.close()

    print(drawings)


choice = "YES"

while choice.upper() == "YES":
    draw()
    choice = input("Do you want to continue to draw winners? Answer Yes or No ")

print("End of drawing")
exit(0)
