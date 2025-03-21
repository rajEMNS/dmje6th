# https://leetcode.com/problems/moving-stones-until-consecutive-ii/description/
import sys

def num_moves_stones_ii(a):
    n = len(a)
    a.sort()

    maxi = 1 - min(a[1] - a[0], a[-1] - a[-2])
    for i in range(1, n):
        maxi += a[i] - a[i - 1] - 1

    mini = sys.maxsize
    j = 0
    for i in range(n):
        while j < n and a[j] - a[i] <= n - 1:
            j += 1
        x = n - j + i
        if x == 1 and a[j - 1] - a[i] == j - i - 1:
            x += 1
        mini = min(mini, x)

    return [mini, maxi]

a = list(map(int, input().strip().split()))
print(num_moves_stones_ii(a))
