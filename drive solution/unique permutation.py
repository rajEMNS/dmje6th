n,k = map(int,input().split())

nums = list(range(1, n + 1))
factorial = 1
for i in range(1, n):
    factorial *= i

k -= 1
result = []

for i in range(n):
    index = k // factorial
    result.append(nums[index])
    nums.pop(index)
    if n - i - 1 != 0:  
        k %= factorial
        factorial //= (n - i - 1)
for i in result:
    print(i,end = "")
