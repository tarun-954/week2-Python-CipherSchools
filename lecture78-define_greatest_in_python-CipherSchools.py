def greater(a,b,c):
    if a > b and a >c:
        return a
    elif b > a and  b>c:
        return b
    else:
        return c
num1=int(input("enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("enter second number:"))
largest=greater(num1,num2,num3)
print(f"{largest} is the greatest number")
