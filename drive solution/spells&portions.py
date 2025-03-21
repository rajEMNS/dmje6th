m, n = map(int, input().split())
spells = list(map(int, input().split()))
potions = list(map(int, input().split()))
success = int(input())

potions.sort(reverse=True)

pairs = []

for spell in spells:
    count = 0
    for potion in potions:
        if spell * potion >= success:
            count += 1
        else:
            break
    pairs.append(count)

for i in pairs:
    print(i, end=" ")
