# function practice
def last_char(a):
    return a[-1]
a=input("Enter your name :")
print(last_char(a))

def odd_number(a):
    if a%2==0:
        return "Even Number"
    elif a%2!=0:
        return "Odd number" 
a=int(input("enter your number :"))
print(odd_number(a))


def odd_number(a):
    if a%2==0:
        return "Even Number"
    return "Odd number" 
a=int(input("enter your number :"))
print(odd_number(a))

def is_even(num):
    if num%2 ==0:
        return True
    return False

def is_even(a):
    return a%2==0
print(is_even(a)) 

def song():
    return "Happy Birtthday song"
print(song)
