def asteroid_collision(asteroids):
    arr = []
    for i in asteroids:
        while arr and arr[-1] > 0 and i <0:
            if arr[-1] < abs(i) :
                arr.pop()
                continue
            if arr[-1] == abs(i):
                arr.pop()
            break
        else:
            arr.append(i)
    return arr  
                

n = int(input())
asteroids = list(map(int, input().split()))
result = asteroid_collision(asteroids)
if result:
    print(" ".join(map(str, result)))
else:
        print("Everything destroyed") 
    