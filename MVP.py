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

# I need to import json file participant1.json - in this file are participants data in json format without weighted
# I need to draw winnings
# User should be able to add input with number of draws
# User should be able to chose if he wants to continue the draw

import json

with open("data/participants1.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

print(jsonObject)
print("How many times to make a draw?")
x = int(input())
drawings = (random.choices(jsonObject, k=x))
drawing = (random.choice(jsonObject))

print(drawings)
selection = input("Do you want to continue to draw winners? Answer Yes or No ")
if selection == "Yes":
    print(drawing)
elif selection == "No":
    print("End of draw")

# I need to import csv file participants2.csv
# I need to draw winings considering the weights
# The grates weight should be drawing the greates number of times

# with open("data/participants2.csv") as csvfile:
#    participants2_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    participants = list(participants2_reader)[1:]
# print(participants)
