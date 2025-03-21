n = int(input())
left, right = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
left_boundary = -1
right_boundary = -1

for i in range(n):
    if nums[i] > right:
        left_boundary = i

    if nums[i] >= left:
        right_boundary = i

    count += right_boundary - left_boundary

print(count)
