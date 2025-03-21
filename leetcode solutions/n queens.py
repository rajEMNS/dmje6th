# https://leetcode.com/problems/n-queens/description/

def solve_N_Queens(n):
    def backtrack(row):
        if row == n:
            solution = []
            for r in board:
                solution.append("".join(r))
            result.append(solution)
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1)
            
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()
    backtrack(0)
    return result

n = int(input().strip())
print(solve_N_Queens(n))
