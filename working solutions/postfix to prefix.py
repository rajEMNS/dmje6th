s = input()
stack = []
operators = ["+","/","-","*"]
for i in s.split():
    if i in operators:
        op2 = stack.pop()
        op1 = stack.pop()
        prefix = i + " " + op1 + " " + op2
        stack.append(prefix)
    else:
        stack.append(i)
        
print(stack[0])