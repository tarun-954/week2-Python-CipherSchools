# solution
def reverse_list(l):
    l.reverse()
    return l
number=[1,2,3,4]
print(reverse_list(number))


def reverse_list(l):
    return l[::-1]
numbers=[1,2,3,4]
print(reverse_list(numbers))

def reverse_list(l):
    r_list=[]
    for i in range(len(l)):
        x=l.pop()
        r_list.append(x)
    return r_list
num2=[1,2,3,4]
print(reverse_list(num2))