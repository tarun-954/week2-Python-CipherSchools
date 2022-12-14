# generate list with range function
num=list(range(1,11))
print(num)

# something about pop method
num=list(range(1,11))
print(num.pop())
print(num)

# index method
num1=[1,2,3,4,5,6,7,8,9,10,1,5,7,9]
print(num1.index(1 ,3,14))

# pass to function
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num1))