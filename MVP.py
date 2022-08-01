# I need to import/load csv file participatnts1 - in this file are participants data without weighted
# I need to draw winnings
# I need to input data with count of participants


import csv
import random
import string

with open("data/participants1.csv") as csvfile:
    participants_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    participants = list(participants_reader)[1:]
print(participants)
print(random.choice(participants))
