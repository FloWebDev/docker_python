import os
from uuid import uuid4

from enum import Enum

# print('Hello World!')

# print(os.path.dirname(os.path.abspath(__file__)))

# i = 1
# for _ in range(10):
#     i_format = f"0{str(i)}" if i < 10 else str(i)
#     print(str(i_format) + ' - ' + uuid4().__str__())
#     i += 1


class Test(Enum):
    ABC = 'abc'
    SUPER = "man"

for t in Test:
    print(t)

print(Test.ABC.value, Test.ABC.name)