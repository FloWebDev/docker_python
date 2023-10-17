# for i in range(0, 10):
#     print(i)

def weird_decorator(function):
    def wrapper():
        print("bbb")
        function()
        function()
        print("ccc")
        function()

    return wrapper


@weird_decorator
def say_aaa():
    print("aaa")

say_aaa()