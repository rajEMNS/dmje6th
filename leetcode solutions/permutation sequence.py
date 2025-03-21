# https://leetcode.com/problems/permutation-sequence/description/

def compute_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def get_permutation(n, k):
    nums = list(range(1, n + 1))
    k -= 1 
    result = []

    for i in range(n):
        fact = compute_factorial(n - 1 - i) 
        index = k // fact
        result.append(str(nums.pop(index)))
        k %= fact
    return ''.join(result)

n = int(input().strip())
k = int(input().strip())
result = get_permutation(n, k)
print(result)

