def checkInclusion(s1,s2):
    if len(s1) > len(s2):
        return False
        
    s1_count = {}
    for char in s1:
        if char in s1_count:
            s1_count[char] += 1 
        else:
            s1_count[char] = 1 
            
    window = {}
    for i in range(len(s1)):
        char = s2[i]
        if char in window:
            window[char] += 1 
        else:
             window[char] = 1 
             
    if s1_count ==  window:
        return True
        
    for i in range(len(s1),len(s2)):
        left = s2[i-len(s1)]
        right = s2[i]
        if right in window:
            window[right] += 1 
        else:
            window[right] = 1 
            
        window[left] -= 1 
        if window[left] == 0:
            window.pop(left,None)
            
            
        if s1_count == window:
            return True
            
    return False
    
s1 = input()
s2 = input()
print (checkInclusion(s1,s2))