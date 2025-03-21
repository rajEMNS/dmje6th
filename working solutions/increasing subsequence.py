def lis(nums):
    if not nums:
        return 1 
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j] +1:
                    dp[i] = dp[j]+1 
    
    max_value = dp[0]
    for i in range(len(dp)):
        if max_value < dp[i]:
            max_value = dp[i]
            
    return max_value
    
n = int(input())
nums = list(map(int,input().split()))
print(lis(nums))  
