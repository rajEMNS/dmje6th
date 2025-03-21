def bubbleSort(candidates):
    n = len(candidates)
    for i in range(n):
        for j in range(0, n-i-1):
            if candidates[j] > candidates[j+1]:
                candidates[j], candidates[j+1] = candidates[j+1], candidates[j]

def combinationSum(candidates, target):
    result = []

    def backtrack(start, target, current_combination):
        if target == 0:
            result.append(list(current_combination))
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, target - candidates[i], current_combination)
            current_combination.pop()

    bubbleSort(candidates)

    backtrack(0, target, [])

    for combination in result:
        print(" ".join(map(str, combination)))

n = int(input())
candidates = list(map(int, input().split()))
target = int(input())

combinationSum(candidates, target)
