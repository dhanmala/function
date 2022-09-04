def max(list):
    max=list[0]
    i=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    return max
list=[3,5,7,34,2,89,2,5]
print("largest value of given list:",max(list))            