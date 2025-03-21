# https://leetcode.com/problems/path-with-maximum-gold/description/


def get_maximum_gold(grid):
    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        original_value = grid[x][y]
        grid[x][y] = 0
        max_gold = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            max_gold = max(max_gold, dfs(x + dx, y + dy))
        grid[x][y] = original_value
        return max_gold + original_value

    max_gold_collected = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                max_gold_collected = max(max_gold_collected, dfs(i, j))
    return max_gold_collected

m, n = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(m)]
print(get_maximum_gold(grid))
