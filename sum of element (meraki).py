def my_sum(numbers):
    total=0
    i=0
    while i<len(numbers):
        total+=numbers[i]
        i=i+1
    return total
numbers=[1,2,38,4,5]    
print(my_sum(numbers))
