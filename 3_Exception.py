def type_errors():
#type error
    print('enter num1:')
    num1 = input()
    print('enter num2:')
    num2 = input()
try:  # keyword used to keep the code segment under check
    print('the sum of these two numbers is', int(num1) + int(num2))
except Exception as e:  # e catch the error ...segment to handle exception after catching it
    print(e)  # e is used to create an instance

print('this line is very important')

# Index Out of Bound exception
try:
    even_numbers = [4, 6, 7, 9]
    print(even_numbers[5])

except IndexError:
    print("Index Out of Bound...")
finally:
    print('This is finally block...')
type_errors()
