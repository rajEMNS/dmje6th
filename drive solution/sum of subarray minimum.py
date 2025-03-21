n = int(input())
arr = list(map(int, input().split()))

stack = []
result = 0
mod = 10**9 + 7
arr = [0] + arr + [0]

for i, x in enumerate(arr):
    while stack and arr[stack[-1]] > x:
        j = stack.pop()
        result += arr[j] * (i - j) * (j - stack[-1])
    stack.append(i)

print(result % mod)
