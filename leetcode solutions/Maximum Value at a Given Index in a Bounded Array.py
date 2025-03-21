# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
def calculate_sum(length, start):
    if length <= start:
        return (start * (start + 1)) // 2 - ((start - length) * (start - length + 1)) // 2
    else:
        return (start * (start + 1)) // 2 + (length - start)

def max_value(n, index, maxSum):
    low, high = 1, maxSum
    while low < high:
        mid = (low + high + 1) // 2
        left_len = index
        right_len = n - index - 1
        
        total = (
            calculate_sum(left_len, mid - 1) +
            calculate_sum(right_len, mid - 1) +
            mid
        )
        
        if total <= maxSum:
            low = mid
        else:
            high = mid - 1

    return low
n, index, maxSum = map(int, input().split())
print(max_value(n, index, maxSum))
