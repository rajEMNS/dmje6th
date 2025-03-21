s1 = input("s1: ")
s2 = input("s2: ")
s3 = sorted(s1)
count = 0

if len(s1) > len(s2):
    print(False)
else:
    for i in range(len(s2) - len(s1) + 1):
        s4 = s2[i:i+len(s1)]
        s4 = sorted(s4)
        if s3 == s4:
            count += 1

    if count > 0:
        print(True)
    else:
        print(False)
