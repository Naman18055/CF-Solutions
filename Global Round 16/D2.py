for _ in range(int(input())):
    n, m = map(int,input().split())

    l = [int(x) for x in input().split()]
    ans = [[l[i], i] for i in range(n * m)]
    ans.sort()
    inconv = 0
    cnt = 0
    for i in range(n):
        lst = ans[i * m:i * m + m]
        lst.sort(key=lambda x: x[1])
        for i in range(m):
            for j in range(i):
                if lst[i][0] > lst[j][0]:
                    cnt += 1
    print(cnt)