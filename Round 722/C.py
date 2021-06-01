# COPIED

import sys
input = sys.stdin.readline
def dfs(u, p, adj, dp0, dp1, lr0, lr1):
    for v in adj[u]:
        if v != p:dfs(v, u, adj, dp0, dp1, lr0, lr1)
    dp0[p] += max(dp0[u] + abs(lr0[p] - lr0[u]),   dp1[u] + abs(lr0[p] - lr1[u]));dp1[p] += max(dp0[u] + abs(lr1[p] - lr0[u]),   dp1[u] + abs(lr1[p] - lr1[u]))
def solve():
    n = int(input());    lr0 = [0] * (n+1);    lr1 = [0] * (n+1);    dp0 = [0] * (n+1);    dp1 = [0] * (n+1);adj = [[] for _ in range(n+1)]
    for i in range(1, n+1):        lr0[i], lr1[i] = map(int, input().split())
    for _ in range(n-1):        u, v = map(int, input().split());      adj[u].append(v);        adj[v].append(u)
    dfs(1, 0, adj, dp0, dp1, lr0, lr1);    print(max(dp0[1], dp1[1]))
for _ in range(int(input())):    solve()