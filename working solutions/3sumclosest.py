def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    
    closest_sum = float('inf')
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1  
            else:
                right -= 1 
    
    return closest_sum

n = int(input())
nums = list(map(int, input().split()))  
target = int(input())  
print(threeSumClosest(nums, target))
