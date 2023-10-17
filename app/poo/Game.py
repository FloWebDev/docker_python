import random as rd

class Game:
    lives = 5
    def __init__(self):
        self.magicNumber = rd.randrange(0, 100)
        print(self.magicNumber)
        self.trials = 0
        self.currentProposition = None
    
    def run(self):
        while(self.trials < Game.lives):
            self.trials += 1
            self.handlePropose()
            self.checkPropose()
        
        print(f"Vous avez perdu! :-(\nLe bon nombre magique était {self.magicNumber}")

    def handlePropose(self):
        self.currentProposition = int(input("Saisissez un nombre entre 0 et 100 : "))
        assert isinstance(self.currentProposition, int) and self.currentProposition >= 0 and self.currentProposition <= 100, "Le nombre doit être compris entre 0 et 100"

    def checkPropose(self):
        if (self.currentProposition < self.magicNumber):
            print("Trop petit")
        elif (self.currentProposition > self.magicNumber):
            print("Trop grand")
        else:
            exit("Gagné ! :-)")