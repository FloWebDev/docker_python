def decorate_function(func):
    def wrapper(*args, **kwargs):
        print('Etape A')
        func(*args, **kwargs)
        print("Etape C")

    return wrapper

def func(arg1, arg2):
    print(f"Etape B {arg1} / {arg2}")

@decorate_function
def funct(arg1, arg2):
    print(f"Etape B {arg1} / {arg2}")

func("Florian", "Vanessa")

print()

func2 = decorate_function(func)
func2("Florian", "Vanessa")

print()

funct("Florian", "Vanessa")

print()
