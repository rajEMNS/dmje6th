def binary(nums,k):
    left = 0
    count = 0
    ones = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            count += 1 
        while count > k:
            if nums[left] == 0:
                count -= 1
            left += 1 
        if ones < right - left +1:
            ones = right - left + 1
    return ones
        

n = int(input())
nums = list(map(int,input().split()))
k = int(input())
print(binary(nums,k)) 