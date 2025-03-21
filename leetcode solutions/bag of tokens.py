# https://leetcode.com/problems/bag-of-tokens/description/
def bagOfTokensScore(tokens, power):
    tokens.sort()
    left, right = 0, len(tokens) - 1
    score = 0
    max_score = 0
    
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break
    
    return max_score

tokens = list(map(int, input().split()))  
power = int(input())  
print(bagOfTokensScore(tokens, power))
