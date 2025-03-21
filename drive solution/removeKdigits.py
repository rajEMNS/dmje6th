num = input()
k = int(input())
stack = []

for i in range(len(num)):
    while stack and k > 0 and stack[-1] > num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])

while k > 0:
    stack.pop()
    k -= 1

while stack and stack[0] == "0":
    stack.pop(0)

result = "".join(stack) if stack else '0'
print("Result:", result)
