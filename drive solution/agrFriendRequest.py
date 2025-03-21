n = int(input())
ages = list(map(int,input().split()))

c = 0
for i in range(n):
    for j in range(n):
        if i != j:
            age1 = ages[i]
            age2 = ages[j]
            
            if age2 <= 0.5 * age1 + 7:
                continue
            if age2 > age1:
                continue
            if age2 > 100 and age1 < 100:
                continue
            c += 1
