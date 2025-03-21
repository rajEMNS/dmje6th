def maxLength(arr):
    def is_unique(s):
        return len(s) == len(set(s))
    
    def backtrack(index, current):
        nonlocal max_length
        if not is_unique(current):
            return
        max_length = max(max_length, len(current))
        for i in range(index, len(arr)):
            backtrack(i + 1, current + arr[i])
    
    max_length = 0
    backtrack(0, "")
    return max_length

n = int(input()) 
arr = [input().strip() for _ in range(n)]

print(maxLength(arr))