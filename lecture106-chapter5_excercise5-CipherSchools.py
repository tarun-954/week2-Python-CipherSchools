def elements(a,b):
    empty=[]
    for i in a:
        if i in b:
            empty.append(i)
    return empty
a=[1,2,5,8]
b=[1,2,7,6]
print(elements(a,b)) 