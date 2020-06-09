n = int(input())
a = list(map(int, input().split()))
d = {}
ans = 1
for i in range(n):
    d[a[i]] = i
mx = d[a[0]]
# print (d)
for i in range(1, n):
    if i > mx:
        ans = (ans<<1)%998244353
    mx = max(mx, d[a[i]])
    # print (ans,mx)
print(ans)