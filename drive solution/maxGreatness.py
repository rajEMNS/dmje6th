n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

ans = 0
for i in range(n):
    if nums[ans] < nums[i]:
        ans += 1

print(ans)
