# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
from collections import Counter

def beautifulSubsets(nums, k):
    def backtrack(index, freq):
        if index == len(nums):
            return 1
        count = backtrack(index + 1, freq)
        num = nums[index]
        if freq[num - k] == 0 and freq[num + k] == 0:
            freq[num] += 1
            count += backtrack(index + 1, freq)
            freq[num] -= 1
        return count
    
    freq = Counter()
    return backtrack(0, freq) - 1

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
print(beautifulSubsets(nums, k))
