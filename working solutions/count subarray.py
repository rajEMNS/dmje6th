def subarray(nums,x):
    count = 0
    length = 0
    for i in nums:
        if i <= x:
            length += 1 
            count += length
        else:
            length = 0
    return count 
    
def boundedMax(nums,left,right):
    return subarray(nums,right) - subarray(nums,left - 1)
    
n = int(input())
left,right = map(int,input().split())
nums = list(map(int,input().split()))
print(boundedMax(nums,left,right))
            