# https://leetcode.com/problems/beautiful-arrangement/description/
def countArrangement(n):
    memo = {}
    
    def backtrack(mask, position):
        if mask == (1 << n) - 1:
            return 1
        
        if (mask, position) in memo:
            return memo[(mask, position)]
        
        count = 0
        for num in range(1, n + 1):
            if (mask & (1 << (num - 1))) == 0:
                if num % position == 0 or position % num == 0:
                    count += backtrack(mask | (1 << (num - 1)), position + 1)
        
        memo[(mask, position)] = count
        return count
    
    return backtrack(0, 1)

n = int(input())  
print(countArrangement(n))
