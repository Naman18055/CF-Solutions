n, x = map(int, input().split())
cur1 = cur2 = cur = res = 0
for a in map(int, input().split()):
    cur1 = max(cur1 + a, 0)
    cur2 = max(cur2 + a * x, cur1)
    print (cur1,end=" ")
    print (cur2)
    cur = max(cur + a, cur2)
    print (cur)
    res = max(res, cur)
print(res)