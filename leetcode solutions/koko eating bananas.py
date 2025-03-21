# https://leetcode.com/problems/koko-eating-bananas/description/
def min_eating_speed(piles, h):
    def can_eat_in_time(k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    low, high = 1, max(piles)
    
    while low < high:
        mid = (low + high) // 2
        if can_eat_in_time(mid):
            high = mid
        else:
            low = mid + 1
    
    return low

n, h = map(int, input().strip().split())
piles = list(map(int, input().strip().split()))
print(min_eating_speed(piles, h))

