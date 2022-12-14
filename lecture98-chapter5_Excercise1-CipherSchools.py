# solution to example 1
def square_num(a):
    sqaure=[]
    for i in a:
        sqaure.append(i**2)
    return sqaure




n=list(range(1,11))
print(square_num(n))