def arrangement(n):
    def dfs(pos):
        if pos > n:
            return 1 
        total = 0 
        for i in range(1,n+1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                total += dfs(pos+1)
                visited[i] =  False
        return total
    visited = [False] * (n+1)
    return dfs(1)
     
n = int(input())
print(arrangement(n))
    