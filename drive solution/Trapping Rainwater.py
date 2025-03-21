arr = list(map(int,input().split()))
res = 0
n = len(arr)

for i in range(1,n-1):
    left = arr[i]
    for j in range(i):
        left = max(left,arr[j])
    right = arr[i]
    for j in range(i+1,n):
        right = max(right,arr[j])

    res += (min(left,right)-arr[i])
print(res)
