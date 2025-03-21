asteroids = list(map(int,input().split()))
arr= []

for i in asteroids:
    while arr and i < 0 < arr[-1]:
        if arr[-1] < -i:
            arr.pop()
            continue
        elif arr[-1 ] == -i:
            arr.pop()
        break
    else:
        arr.append(i)
print(arr)
