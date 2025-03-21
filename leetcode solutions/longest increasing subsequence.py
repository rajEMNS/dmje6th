# https://leetcode.com/problems/longest-increasing-subsequence/

def length_of_LIS(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n = int(input().strip())
nums = list(map(int, input().strip().split()))
print(length_of_LIS(nums))
