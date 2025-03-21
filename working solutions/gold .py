def get_maximum_gold(grid):
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        original_value = grid[x][y]
        grid[x][y] = 0 
        max_gold = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            collected = dfs(x + dx, y + dy)
            if collected > max_gold:
                max_gold = collected
        grid[x][y] = original_value 
        return max_gold + original_value

    max_gold_collected = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                collected = dfs(i, j)
                if collected > max_gold_collected:
                    max_gold_collected = collected
    return max_gold_collected

m, n = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(m)]
print(get_maximum_gold(grid))