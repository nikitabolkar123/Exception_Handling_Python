def A(a, b):
    try:
        c = ((a + b) / (a - b))
    except Exception as e:
        print(e)
    else:
        print(c)
    finally:
        c = a + b
        print('Finally = ', c)


A(2.0, 3.0)
A(3.0, 3.0)