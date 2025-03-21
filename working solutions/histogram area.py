def histogram(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area,h*width)
        stack.append(i)
        
    while stack: 
        h = heights[stack.pop()]
        width = n if not stack else n - stack[-1] -1
        max_area = max(max_area,h*width)
    return max_area

n = int(input())
heights = list(map(int,input().split()))
print(histogram(heights))
