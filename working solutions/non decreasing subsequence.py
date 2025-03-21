def findSubsequences(nums):
    def backtrack(start, path):
        if len(path) >= 2:
            result.add(tuple(path))  
        
        for i in range(start, len(nums)):
            if not path or nums[i] >= path[-1]:
                backtrack(i + 1, path + [nums[i]])

    result = set()  
    backtrack(0, [])  
    return sorted(result) 

n = int(input()) 
nums = list(map(int, input().split())) 

subsequences = findSubsequences(nums)
for subseq in subsequences:
    print(" ".join(map(str, subseq)))