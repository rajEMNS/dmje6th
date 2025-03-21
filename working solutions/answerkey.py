ans = input()
k = int(input())
left = 0
max_length = 0
count = 0
for right in range(len(ans)):
    if ans[right] != 'T':
        count += 1 
    else: 
        count = 1 
        
    while count > 2:
        if ans[left] != 'T':
            count -= 1 
        left+= 1 
    max_length = max(max_length,right-left +1)
    
left = 0
count = 0
for right in range(len(ans)):
    if ans[right] != 'F':
        count += 1 
    else:
        count = 1 
        
    while count > 2:
        if ans[left] != 'F':
            count -= 1 
        left += 1 
    max_length = max(max_length,right -left+1)
print(max_length)