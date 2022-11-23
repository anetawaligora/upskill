import csv
import json


def parse_json(file):
    return json.load(file)


def parse_json_weighted(file):
    participants = json.load(file)
    return list(participants)


def parse_csv(file):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    return list(participants_reader)[1:]


def parse_csv_weighted(file):
    participants_reader = csv.reader(file, delimiter=',', quotechar='|')
    return list(participants_reader)[1:]

#def parse_json_prizes(file):
#    prizes = json.load(file)
#    return list(prizes)