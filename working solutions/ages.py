def request(ages):
    def can_send_request(x,y):
        if y <= 0.5 * x + 7:
            return False
        if y > x:
            return False
        if y > 100 and x < 100 :
            return False
        return True
        
    count = 0 
    for i in range(len(ages)): 
        for j in range(len(ages)):
            if i != j and can_send_request(ages[i],ages[j]):
                count += 1 
    return count
n = int(input())
ages = list(map(int,input().split()))
print(request(ages))