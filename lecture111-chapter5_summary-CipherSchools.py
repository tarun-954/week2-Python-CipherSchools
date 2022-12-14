def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You cannot divide a number by zero")
    except TypeError as err:
        print("Unexpected error")
print(divide(10,0))