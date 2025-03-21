n = int(input())
queens = []
xy_dif = []
xy_sum = []
result = []
p = 0
q = 0

stack = [(queens, xy_dif, xy_sum, p)]  

while stack:
    queens, xy_dif, xy_sum, p = stack.pop()
    if p == n:
        result.append(queens)
    else:
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                stack.append((queens + [q], xy_dif + [p - q], xy_sum + [p + q], p + 1))

formatted_result = [["." * i + "Q" + "." * (n - i - 1) for i in sol ] for sol in result]

for solution in formatted_result:
    for row in solution:
        print(row)
