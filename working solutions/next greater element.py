def next_greater_element(nums1, nums2):
    result = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            result[stack.pop()] = num
        stack.append(num)
        
    while stack:
        result[stack.pop()] = -1
        
    return [result[num] for num in nums1]

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
result = next_greater_element(nums1, nums2)
print(" ".join(map(str, result)))
