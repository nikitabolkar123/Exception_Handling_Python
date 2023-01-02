def mul_errors():


    try:
        # code block where exception can occurs
        a = int(input('enter the number 1:'))
        b = int(input('enter the number 2:'))
        c = a / b
        d = a * b
        e = a / b
        print(c)
        print(d)
        print(e)
    except NameError:
        print('the user have not defined the variable:')
    except ZeroDivisionError:
        print('please provide number greater than 0')
    except TypeError:
        print('Try to make the datatype similar')
    except Exception as ex:
        print(ex)
    else:
        print(c)
        print(d)
        print(e)
    finally:
        print('The Execution is done!')
mul_errors()
