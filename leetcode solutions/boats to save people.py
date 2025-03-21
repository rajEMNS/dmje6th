# https://leetcode.com/problems/boats-to-save-people/description/

def num_rescue_boats(people, limit):
    def manual_sort(people):
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                if people[i] > people[j]:
                    people[i], people[j] = people[j], people[i]

    manual_sort(people)
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats

n, limit = map(int, input().strip().split())
people = list(map(int, input().strip().split()))
print(num_rescue_boats(people, limit))
