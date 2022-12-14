fruits=["mango","grapes"]
fruits.insert(1,"oranges")
print(fruits)

fruit1=["grapes","apple"]
fruit2=fruits + fruit1
print(fruit2)

# extand method
fruits.extend(fruit1)
print(fruits)

fruits.append(fruit1)
print(fruits)