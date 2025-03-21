def permute(nums):
    def get_permutations(nums,start):
        if start == len(nums)-1:
            res.append(nums[:])
            return
        for i in range(start,len(nums)):
            nums[i],nums[start] = nums[start] ,nums[i]
            get_permutations(nums,start +1)
            nums[i],nums[start] = nums[start] ,nums[i]
            
    res = []
    get_permutations(nums,0)
    return res
    
def sort(a):
    n = len(a) 
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

n = int(input())
nums = list(map(int,input().split()))
result = permute(nums)
sort(result)
for i in result:
    print(" ".join(map(str,i))) 

        