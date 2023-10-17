import random as rd

res = rd.randrange(0, 100)
print(res)

life = 0

while (life < 5):
    life += 1

    propose = int(input("Saisissez un nombre entre 0 et 100 : "))

    assert isinstance(propose, int) and propose >= 0 and propose <= 100, "Le nombre doit être compris entre 0 et 100"

    if (propose < res):
        print("Trop petit")
    elif (propose > res):
        print("Trop grand")
    else:
        exit("Gagné ! :-)")

print(f"Vous avez perdu! :-(\nLe bon nombre magique était {res}")
