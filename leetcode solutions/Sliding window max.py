# https://leetcode.com/problems/sliding-window-maximum/
def maxSlidingWindow(nums, k):
    result = []
    window = []
    
    for i in range(len(nums)):
        if window and window[0] < i - k + 1:
            window.pop(0)
        
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        
        window.append(i)
        
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

nums = list(map(int, input().split()))
k = int(input())
print(maxSlidingWindow(nums, k))

