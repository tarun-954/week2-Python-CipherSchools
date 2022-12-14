# for loop in string formating 
name="tarun"
for i in range(len(name)):
    print(name[i])

name="tarun"
for i in name:
    print(i)

# 1256----->1+2+3+4
num=input("Enter a number:")
total=0
for i in num:
    total+=int(i)
print(total)