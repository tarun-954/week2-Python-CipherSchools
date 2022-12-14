# soltuions
def even_odd_num(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)

    output=[odd_nums ,even_nums]
    return output
num=[1,2,3,4,5,6,7]
print(even_odd_num(num))







