from collections import deque, defaultdict

def pushDominoes(dominoes):
    dominoes = list(dominoes)
    queue = deque()
    
    for i, state in enumerate(dominoes):
        if state == "L" or state == "R":
            queue.append((i, state))
    
    while queue:
        local_collisions = defaultdict(list)
        
        for _ in range(len(queue)):
            i, state = queue.popleft()
            
            if state == "L":
                if i >= 1 and dominoes[i-1] == ".":
                    local_collisions[i-1].append("L")
            else:
                if i < len(dominoes) - 1 and dominoes[i+1] == ".":
                    local_collisions[i+1].append("R")
        
        for i, states in local_collisions.items():
            if len(states) == 2:
                dominoes[i] = "."
            elif len(states) == 1:
                dominoes[i] = states[0]
                queue.append((i, states[0]))

    return "".join(dominoes)

dominoes = input()
print(pushDominoes(dominoes)) 