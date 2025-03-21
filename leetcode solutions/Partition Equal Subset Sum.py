# https://leetcode.com/problems/partition-equal-subset-sum/description/
def canPartition(nums):
    target = sum(nums)
    if target % 2:
        return False
    target = target // 2

    if nums[0] == target:
        return True
    
    dp = set([nums[0]])
    for i in nums[1:]:
        new_dp = set()
        for s in dp:
            new_dp.add(s)
            new_dp.add(s + i)
        if target in new_dp:
            return True
        dp = new_dp
    
    return False

nums = list(map(int, input().split()))
print(canPartition(nums))
