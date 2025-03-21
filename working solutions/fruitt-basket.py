def fruit_basket(n,fruits):
    count = {}
    left = 0
    max_fruits = 0
    for right in range(n):
        if fruits[right] in count:
            count[fruits[right]] += 1 
        else:
            count[fruits[right]] = 1 
            
    while len(count) > 2:
        count[fruits[left]] -=1  
        if count[fruits[left]] == 0:
            count.pop(fruits[left],None)
        left += 1 
        
    x = right - left +1
    if x > max_fruits:
        max_fruits = x  
    return max_fruits
     
n = int(input())
fruits = list(map(int,input().split()))
print(fruit_basket(n,fruits))