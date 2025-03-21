# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
def numSubarrayBoundedMax(nums, left, right):
    
    def count_subarrays_with_max_atmost_x(x):
        front = count = 0

        for rear in range(len(nums)):
            if nums[rear] > x:
                front = rear + 1
                continue
            count += rear - front + 1

        return count
    
    return count_subarrays_with_max_atmost_x(right) - count_subarrays_with_max_atmost_x(left - 1)

nums = list(map(int, input().split()))
left, right = map(int, input().split())
print(numSubarrayBoundedMax(nums, left, right))
