for t in range(int(input())):
    input()  # empty line
    n, k = map(int, input().rstrip().split())
    E = [[] for i in range(n)]
    EV = [0] * n
    for i in range(n - 1):
        x, y = map(lambda x: int(x) - 1, input().rstrip().split())
        E[x].append(y)
        E[y].append(x)
        EV[x] += 1
        EV[y] += 1
    if n == 1:
        print(0)
        continue
    ans = n
    pool = [v for v in range(n) if EV[v] == 1]
    while k and pool:
        newpool = []
        for v in pool:
            for vv in E[v]:
                EV[vv] -= 1
                if EV[vv] == 1:
                    newpool.append(vv)
        ans -= len(pool)
        pool = newpool
        k -= 1
    print(ans)
