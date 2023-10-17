from abc import ABC

class A(ABC):
    counterA = 0
    def __init__(self) -> None:
        print(self.__class__.__name__)
        self.counterB =+ 3
        A.counterA = 5

class B(A):
    def __init__(self) -> None:
        self.counterB = 0
        super().__init__()
    
    def getParentCounter(self):
        return super().counterA


inst = B()

# print(inst.counterB)
# print(inst.getParentCounter())

help(B)