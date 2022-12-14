# practive for loop 
# ask user name and count each character
# "tarun choudhary"
name=input("Enter your name:")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")

