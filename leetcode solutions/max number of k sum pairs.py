# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
from collections import Counter

def maxOperations(nums, k):
    freq = Counter(nums)
    operations = 0
    
    for num in list(freq):  
        complement = k - num
        if complement in freq:
            if num == complement:
                operations += freq[num] // 2
            else:
                pairs = min(freq[num], freq[complement])
                operations += pairs
                freq[num] -= pairs
                freq[complement] -= pairs
    return operations

nums = input().split()  
nums = [int(x) for x in nums]  
k = int(input())  
print(maxOperations(nums, k))

