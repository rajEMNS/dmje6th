# https://leetcode.com/problems/subsets/description/
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result


nums = list(map(int, input().split()))
print(subsets(nums))
