# https://leetcode.com/problems/maximize-greatness-of-an-array/description/

def maximize_greatness(nums):
    def sort(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    sort(nums)
    count = 0
    j = 0
    for i in range(len(nums)):
        if nums[j] < nums[i]:
            count += 1
            j += 1
    return count

n = int(input().strip())
nums = list(map(int, input().strip().split()))
print(maximize_greatness(nums))
