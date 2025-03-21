# https://leetcode.com/problems/maximum-length-of-pair-chain/
def findLongestChain(pairs):
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if pairs[i][1] > pairs[j][1]:
                pairs[i], pairs[j] = pairs[j], pairs[i]

    current_end = float('-inf')
    chain_length = 0

    for a, b in pairs:
        if a > current_end:
            chain_length += 1
            current_end = b

    return chain_length

n = int(input())  
pairs = []
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append([a, b])

print(findLongestChain(pairs))

