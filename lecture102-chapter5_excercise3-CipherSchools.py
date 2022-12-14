def reverse_list(a):
    empty=[]
    for i in a:
        a=empty.append(i[::-1])
    return empty



a=["abc","tuv","xyz"]
print(reverse_list(a))
