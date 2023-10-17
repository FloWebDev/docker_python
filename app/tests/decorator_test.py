# from random import randint

# def decorator_sum(function):
#     def wrapper(*args, **kwargs):
#         increment = randint(1,10)

#         result = function(*args, **kwargs)

#         result += increment
#         return result

#     return wrapper

# @decorator_sum
# def sum(first_number: int|float, second_number):
#     return first_number + second_number

# result = sum(3, 4)
# print(result)

# print()

# sum_decorator = decorator_sum(sum)
# result = sum_decorator(3, 4)
# print(result)

class A:
    def sum(self, first_number: int|float, second_number):
        return first_number + second_number

class DecoratorA:
    def __init__(self, classToDecorate) -> None:
        self.classToDecorate = classToDecorate
    
    def getInstance(self, *args, **kwargs):
        print('Traitement avant')
        print('-------------------')
        inst = self.classToDecorate(*args, **kwargs)
        print('Traitement après')
        return inst

inst1 = A()
res = inst1.sum(17, 33)
print(res)

print()

inst2 = DecoratorA(A).getInstance()
res = inst2.sum(17, 34)
print(res)