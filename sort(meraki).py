a=[4,8,7,2,3,8,9]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            a[i],a[j]=a[j],a[i]
print(a)            