people = list(map(int, input().split()))
limit = int(input())
people.sort()
i = 0
j = len(people) - 1
count = 0
while i <= j:
    if people[i] == limit or people[i] + people[j] <= limit:
        i += 1
    j -= 1
    count += 1
print(count)
