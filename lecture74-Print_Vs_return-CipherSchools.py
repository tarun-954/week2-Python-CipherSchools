# print vs return function
def add_three(a,b,c):
    return a+b+c
print(add_three(10,20,30))

def add_three(a,b,c):
    print(a+b+c)
add_three(10,20,30)