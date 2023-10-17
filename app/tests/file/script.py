# with open("test.txt", "w") as file:
#     index = 0
#     while index < 10:
#         index += 1
#         file.write(f"voici la phrase n° {index}\n")

import csv
import random

perso_list = [
    {"first_name": "Florian", "last_name": "Mathevon", "age": 37, "random": random.randint(0, 100)},
    {"first_name": "Vanessa", "last_name": "Mathevon-Balas", "age": 38, "random": random.randint(0, 100)},
    {"first_name": "Gabriel", "last_name": "Mathevon", "age": 7, "random": random.randint(0, 100)},
    {"first_name": "Charlotte", "last_name": "Mathevon", "age": 5, "random": random.randint(0, 100)},
]

# header = []
# for title in perso_list[0].keys():
#     header.append(title)

# with open('eggs.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=perso_list[0].keys())
#     writer.writeheader()
#     writer.writerows(perso_list)


csvfile = open('eggs.csv', 'w')
writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=perso_list[0].keys())
writer.writeheader()
writer.writerows(perso_list)
csvfile.close()