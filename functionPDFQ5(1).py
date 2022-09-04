def unique_list(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
        return a
    final=[]
    for j in a:
        b=list.count(j)
        if b==1:
            final.append(j)
        return final
print(unique_list([1,1,2,2,3,4,4,5,5,7]))          
