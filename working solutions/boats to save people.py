def rescue(people,limit):
    def sort(a):
        n = len(a)
        for i in range(n):
            for j in range(n-i-1):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j] 
                    
    sort(people)
    left = 0
    right = len(people)-1 
    boats = 0
    while left <= right:
        if people[right] +people[left] <= limit:
            left += 1  
        right -= 1 
        boats += 1 
    return boats  
     
n,limit= map(int,input().split())
people = list(map(int,input().split()))
print(rescue(people,limit))
            