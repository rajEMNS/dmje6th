n, k = map(int,input().split())
arr = list(map(int,input().split()))
res = []
for i in range(n):
    for j in range(i+1,n):
        res.append((arr[i],arr[j]))

res.sort(key = lambda x: x[0]/x[1])
nume,deno = res[k-1]
print(nume,deno)
