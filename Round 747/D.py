class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def solve():
    n, m = map(int, input().split())
    dsu = DisjointSetUnion(2*n)
    for i in range(m):
        x, y, z = map(str, input().split())
        x = int(x) - 1
        y = int(y) - 1
        if z == "imposter":
            dsu.union(x, y+n)
            dsu.union(x+n, y)
        else:
            dsu.union(x, y)
            dsu.union(x+n, y+n)
    for i in range(n):
        if dsu.find(i) == dsu.find(i+n):
            return -1
    g = [[] for i in range(2*n)]
    for i in range(2*n):
        g[dsu.find(i)].append(i)
    ans = 0
    for a in g:
        cur = sum(i<n for i in a)
        ans += max(cur, len(a)-cur)
    return ans // 2


import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    print(solve())