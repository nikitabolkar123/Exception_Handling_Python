def divide():
    a = 10
    b = 0
    try:
        d = a / b
        print(d)

    except ZeroDivisionError:
        print('Division by zero not allowed')

    else:  # run when no exception exist
        print('Inside else')
    finally:  # it will execute exception occurs or not
        print('inside finally')

print('rest of code')
divide()
