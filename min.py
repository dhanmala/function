def min(a):
   min=a[0]
   i=0
   while i<len(a):
      if a[i]<min:
         min=a[i]
      i+=1
   return min
a=[8,6,4,8,4,50,2,7]
print(min(a))         
