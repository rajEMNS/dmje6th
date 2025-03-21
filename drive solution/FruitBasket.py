n = int(input())
fruits = list(map(int,input().split()))

basket = {}
maxlength = 0
j = 0

for i in range(n):
    if fruits[i] in basket:
        basket[fruits[i]] += 1
    else:
        basket[fruits[i]] = 1


    while len(basket)>2:
        basket[fruits[j]] -= 1
        if basket[fruits[j]]== 0:
            del basket[fruits[j]]
        j+=1
maxlength = max(maxlength, i - j + 1)
print(maxlength)
