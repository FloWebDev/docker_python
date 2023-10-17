class Fish:
    pass

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def walk(self):
        print(self.name + " walks!")
    
    @staticmethod
    def getTotalPopulation():
        print("Population is about 7 billions of people")

my_list = [Person("Florian"), Person("Vanessa"), Person("Gabriel"), Person("Charlotte")]

for person in my_list:
    person.walk()

Person.getTotalPopulation()


my_tuple = ('1', "toto", "ok", 'True', 'Person("Toto")')

print(' - '.join(my_tuple))