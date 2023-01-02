# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid")

#class Error is derived from super class Exception
class Error(Exception):
    pass


class DobException(Error):
    pass


def check_age():
    year = int(input("Enter year of birth : "))
    age = 2022 - year
    try:
        if 20 <= age <= 30:
            print("You are eligible")
        else:
            raise DobException
    except DobException:
        print("You are not eligible")


check_age()














# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid")