user_info={
    "name":"tarun",
    "age": 19,
    "fav_movies":["coco","avenger"],
    "fav_tunes":["awaking","Fairy tale"],
}
if "name" in user_info:
    print("present")
else:
    print("not present")

    # key is mostly string or int

if 24 in user_info.values():
    print("not present")
else:
    print("not present")

for i in user_info:
    print(i)

user_info_keys=user_info.keys()
print(user_info)
# loops in dictionaries:
for i in user_info:
    print(user_info)
user_items=user_info.items()
print(user_info)
print(type(user_items))
[("name","tarun"),("age","19"),("fav_,movies","kiwi no na wa")]
for i,j in user_info.items():
    print(f"key is {i} and value is {j}")
    print(i)