from abc import ABC, abstractmethod  # permet de définir des classes de base

class Shape(ABC):
    def area(self):
        return 0
    
    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
    def perimeter(self):
        return self.length * 4
    
sqr = Square(4)
area = sqr.area()

print(area)
print(sqr.perimeter())

default_value = 777

test_dico = {"simple": 1, "serré": 1, "allongé": 1.5}
res = test_dico.get("allongé", default_value)
print(res)