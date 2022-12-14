#if statement
name="tarun"
if name =="traun" or name=="Tarun":
    print("You are tarun")
elif name=="vaishu" or name=="Vaishu":
    print("you are vaishu")
else:
    print("You are not tarun nor vaishu ")


# while loop in python
i =0
while i <10:
    print("Hello world")
    i=i+1
# for loop
for i in range(1,11,2):
    print(i)

# break statement
for i in range(1,11):
    if i==5:
        break
    print(i)

# continue statement
for i in range(1,11):
    if i==5:
        continue
    print(i)

# printing single single charcter in string in python
for i in "tarun":
    print(i)
