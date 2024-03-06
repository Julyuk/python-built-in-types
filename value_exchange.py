def value_exchanger(a,b):
    print("Initial a value is: ", a)
    print("Initial b value is: ", b)
    a, b = b, a
    print("New a value is: ", a)
    print("New b value is: ", b)


value_exchanger(1,2)