# definig a PALINDROM number 
def ispalindrome(a):
    if a[::-1]==a[::1]:
        return True
    else:
        return False
a=input("Enter any value")
print(ispalindrome(a))