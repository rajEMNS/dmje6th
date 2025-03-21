piles = list(map(int, input().split()))
h = int(input())

i, j = 1, max(piles)

while i < j:
    mid = (i + j) // 2
    if sum((pile - 1) // mid + 1 for pile in piles) <= h:
        j = mid
    else:
        i = mid + 1
print(i)
