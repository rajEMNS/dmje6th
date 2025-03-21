# https://leetcode.com/problems/non-decreasing-subsequences/

def find_subsequences(nums):
    result = []

    def backtrack(start, path):
        if len(path) > 1:
            result.append(path[:])
        
        visited = [False] * 201
        for i in range(start, len(nums)):
            if (not path or nums[i] >= path[-1]) and not visited[nums[i] + 100]:
                visited[nums[i] + 100] = True
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
    
    backtrack(0, [])
    return result

nums = list(map(int, input().split()))
print(find_subsequences(nums))
