# fromkeys
d={"name":"unknown","age":"unknown"}
d=dict.fromkeys(("name","age","height"),"unknown")
print(d)

d=dict.fromkeys((range(1,11)),"unknown")
print(d)

# get method(useful)

d={"name":"unknown","age":"unknown"}
print(d["name"])
print(d.get("name")) 
if "name" in d:
    print("present")
else:
    print("Not present")
# if None ----False , els---->trueeeeeeeee
# d.clear()
# print(d)
d1=d.copy()
d1=d
print(d1.popitem())
print(d)

print(d1 is d)