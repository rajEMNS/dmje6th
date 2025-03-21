def maximise_greatness(nums):
    def sort(a):
        n = len(a)
        for i in range(n):
            for j in range(n-i-1):
                if a[j]> a[j+1]:
                    a[j],a[j+1]= a[j+1],a[j]
                    
    sort(nums)
    j = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] >nums[j]:
            count += 1 
            j+=1
    return count    
    
n = int(input())
nums = list(map(int,input().split()))
print(maximise_greatness(nums))