s = input()
stack = []
operators = ["+","-","/","*"]
for i in s.split():
    if i in operators:
        op2 = stack.pop(len(stack)-1)
        op1 = stack.pop(len(stack)-1)
        infix = "(" + op1 +" "+i+" "+op2+")"
        stack.append(infix)
    else:
        stack.append(i)
        
result = stack[len(stack)-1] 
print(result)    