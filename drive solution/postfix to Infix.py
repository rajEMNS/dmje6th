str1 = input()
arr = []
operators = ["+", "-", "*", "/"]

for i in str1.split():
    if i in operators:
        op2 = arr.pop(len(arr) - 1)
        op1 = arr.pop(len(arr) - 1)
        infix = "(" + op1 + i + op2 + ")"
        arr.append(infix)
    else:
        arr.append(i)

result = arr[len(arr) - 1]
print(result)
