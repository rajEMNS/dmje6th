def num_moves_stones_ii(a):
    n = len(a)
    
    # Sorting the array manually using bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
    maxi = 1 - min(a[1] - a[0], a[-1] - a[-2])
    for i in range(1, n):
        maxi += a[i] - a[i - 1] - 1

    # Finding the minimum using a basic comparison method
    mini = None  # Start with None
    j = 0
    for i in range(n):
        while j < n and a[j] - a[i] <= n - 1:
            j += 1
        x = n - j + i
        if x == 1 and a[j - 1] - a[i] == j - i - 1:
            x += 1
        if mini is None or x < mini:  # Compare and update mini
            mini = x

    return [mini, maxi]

n = int(input())
a = list(map(int, input().strip().split()))
result = num_moves_stones_ii(a)

print(*result)
