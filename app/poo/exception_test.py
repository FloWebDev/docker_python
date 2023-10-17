# import traceback

# def increase_percent(initial_value, after_value):
#     try:
#         return (after_value / initial_value) * 100
#     except ZeroDivisionError:
#         # print(traceback.format_exc())
#         return 0
#     except Exception as error:
#         print("Uh oh, unexpected error occurred!")
#         raise error

# print(increase_percent(2, 17))
# print(increase_percent(0, 17))

class PersonException(Exception):
    pass


class InvalidDOBPersonException(PersonException):
    pass


try:
    raise InvalidDOBPersonException("Invalid Date of Birth")
except PersonException:
    print("PersonException caught")
except InvalidDOBPersonException("Invalid Date of Birth"):
    print("InvalidDOBPersonException caught")
except Exception:
    print("Exception caught.")