# https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    while stack:
        next_greater[stack.pop()] = -1
    
    result = []
    for num in nums1:
        if num in next_greater:
            result.append(next_greater[num])
        else:
            result.append(-1)
    return result
n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
result = nextGreaterElement(nums1,nums2)
print(" ".join(map(str,result)))
