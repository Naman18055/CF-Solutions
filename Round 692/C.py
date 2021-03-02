for _ in range(int(input())):
    n,m = map(int,input().split())
    par = [i for i in range(n+1)]
    def find(x):
        if par[x]==x:return x
        par[x] = find(par[x])
        return par[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x==y: return 1
        par[x] = y
        return 0
    res = 0
    for i in range(m):
        x,y = map(int,input().split())
        if x==y: continue
        res+=1+union(x,y)
    print(res)