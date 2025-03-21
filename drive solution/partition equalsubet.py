A = list(map(int,input().split()))
total = sum(A)

if total % 2 != 0:
    print("false")
else:
    t = total // 2
    P = set([0])

    for x in A:
        for y in list(P):
            P.add(x + y)

    if t in P:
        print("true")
    else:
        print("false")
