# https://leetcode.com/problems/fruit-into-baskets/description/
fruits = list(map(int, input().split()))
fruit_count = {}
left = 0
max_fruits = 0
for right in range(len(fruits)):
    fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
    while len(fruit_count) > 2:
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1
    max_fruits = max(max_fruits, right - left + 1)
print(max_fruits)
