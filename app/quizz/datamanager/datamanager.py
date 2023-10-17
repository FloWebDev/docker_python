import os
import csv
from random import randint

def getRandomQuestion():
    questions = _getData()
    randomIndex = randint(0, len(questions) - 1)
    return questions[randomIndex]

def _getData():
    questions = []
    dataPath = os.path.dirname(os.path.abspath(__file__)) + "/../data/data.csv"
    with open(dataPath, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            questions.append(row)
    return questions

