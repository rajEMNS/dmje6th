# https://leetcode.com/problems/friends-of-appropriate-ages

def numFriendRequests(ages):
    n = len(ages)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ages[j] > ages[j + 1]:
                ages[j], ages[j + 1] = ages[j + 1], ages[j]
    
    this_age_cnt = 0
    prev_age = ages[0]
    left = 0
    requests_count = 0
    
    for right, age in enumerate(ages):
        while left < right and ages[left] <= age * 0.5 + 7:
            left += 1
        requests_count += right - left
        if age == prev_age:
            this_age_cnt += 1
        else:
            if prev_age > 14:
                requests_count += this_age_cnt * (this_age_cnt - 1) // 2
            this_age_cnt = 1
            prev_age = age
    
    if prev_age > 14:
        requests_count += this_age_cnt * (this_age_cnt - 1) // 2
    
    return requests_count

ages = list(map(int, input().split()))

print(numFriendRequests(ages))
