user_info={
    "name":"tarun",
    "age": 19,
    "fav_movies":["coco","avenger"],
    "fav_tunes":["awaking","Fairy tale"]
    # how to add data
} 
user_info["fav_songs"]=["song1","song2"]
print(user_info)

# pop method
popped_item=user_info.pop("fav_tunes")
print(f"popped item is{popped_item}")
print(user_info)


# pop item method

popped_item=user_info.popitem()
print(user_info)
print(type(popped_item))