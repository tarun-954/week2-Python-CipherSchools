# dictionaries intro
# unordered collection of data in key
# hoe to create dictories
user={"name":"tarun","age":19}
print(user)
print(type(user))

# second mrtod to create dictonaries
user1=dict(name="tarun",age=19)
print(user)
print(type(user))

# keys used to access the data 
print(user["name"])
print(user["age"])



user_info={
    "name":"tarun",
    "age": 19,
    "fav_movies":["coco","avenger"],
    "fav_tunes":["awaking","Fairy tale"]
}
print(user_info["fav_movies"])

# how to add data to empty dictionary
user_info2={}
user_info2["name"]="tarun"
user_info["age"]=19
print(user_info2)
