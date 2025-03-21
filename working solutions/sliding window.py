def sliding_window(nums,k):
    result = []
    window = []
    for i in range (len(nums)):
        if window and window[0] < i - k + 1:
            window.pop(0)
        while window and nums[window[-1]]  < nums[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])
            
    return result

n = int(input())
nums = list(map(int,input().split()))
k = int(input())
result = sliding_window(nums,k)
print(" ".join(map(str,result)))    