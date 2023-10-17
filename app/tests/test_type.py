class SpecificError(Exception):
    pass

def test(arg1: int, arg2: int):
    if not isinstance(arg1, int) or not isinstance(arg2, int):
        raise SpecificError("NOP !")
    return arg1 + arg2

res = test(int(('15')), 10)

print(res)


