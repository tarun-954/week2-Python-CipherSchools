# looping in tuples
# tuple in one elemnt
# tuple without paranthes
# tuple unpacking
# list  inside tuple
# some function that you can use with tuples 
mixed=(1,2,3,4.0)
# for loop in tuple
for i in mixed:
    print(i)

# tuple with one element
num=(1,)
words=("word1")
print(type(num))

# tuple without paranthese
guitars="yamaha","baton rouge","tylor"
print(type(guitars))

# tuple unpacking
guiterist=("tarun","vaishu","sejal")
guiterist1,guiterist2,guiterist3=(guiterist)
print(guiterist2)

# list inside tuple
x=("abc",["bcd"])
x[1].append("xyz")
print(x)