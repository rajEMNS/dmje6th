def generate_parenthesis(n):
    def backtrack(s="",left = 0,right = 0):
        if len(s) == 2*n:
            res.append(s)
            return
        if left<n:
            backtrack(s+"(",left +1,right)
        if right < left:
            backtrack(s+")",left,right +1)
            
    res = []
    backtrack() 
    return res
 
n = int(input())
result = generate_parenthesis(n)
for i in result:
    print(i,end= " ") 