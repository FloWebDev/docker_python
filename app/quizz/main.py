from datamanager import getRandomQuestion
from random import shuffle

question = getRandomQuestion()
answers = [
    question['answer_1'],
    question['answer_2'],
    question['answer_3'],
    question['answer_4']
]

shuffle(answers)

print(question['question'])

print()

nbQuestion = 1
for answer in answers:
    print(f"{nbQuestion}) {answer}")
    nbQuestion += 1

print()

while True:
    propo = input("Choisissez entre 1, 2, 3 ou 4 : ")
    print()
    if propo in ["1", "2", "3", "4"]:
        propo = answers[int(propo) - 1]
        break

if propo == question['answer_1']:
    print("Bravo ! C'est gagné !")
else:
    print(f"Perdu ! La bonne réponse est {question['answer_1']}")

print()
