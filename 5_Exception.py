def even():
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except:
        print("Not an even number!")
    else:
        reciprocal = 1 / num
        print(reciprocal)


even()


print("******************************************************")


def my_tuple():
  prices = { 'Pen' : 10, 'Pencil' : 5, 'Notebook' : 25}
  item = input('Get price of: ')
  try:
    print(f'The price of {item} is {prices[item]}')
  except KeyError:
    print(f'The price of {item} is not known')
  finally:
    print(f'The finally statement is executed')
my_tuple()


print("******************************************************")

def name_error():
#Name Error
    try:
        print('x')
    except:
        print('something went wrong')
    finally:
        print('finally block')
name_error()
#help(Exception)
#2ndprogram
def fun(a):
    if a < 4:
        b = a / (a - 3)
        print("Value of b = ", b)

try:
    fun(3)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")s