def dividePlayers(skill):
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    
    bubble_sort(skill)
    
    n = len(skill)
    if n % 2 != 0:
        return -1
    
    pair_sum = skill[0] + skill[-1]
    total_product = 0
    
    for i in range(n // 2):
        if skill[i] + skill[n - i - 1] != pair_sum:
            return -1
        total_product += skill[i] * skill[n - i - 1]
    
    return total_product

n = int(input())
skill = list(map(int, input().split()))
print(dividePlayers(skill))
