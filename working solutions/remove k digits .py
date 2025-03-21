def maxOperations(nums,k):
    freq = {}
    count = 0
    for i in nums:
        complement = k - i 
        if complement in freq and freq[complement] > 0:
            freq[complement] += 1 
            count += 1 
        else:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1 
                
    return count 
        
n,k = map(int,input().split())    
nums = list(map(int,input().split()))
print(maxOperations(nums,k))
                
          