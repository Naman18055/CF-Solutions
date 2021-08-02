import sys
input = sys.stdin.readline

for nt in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    curr = [0]
    for i in range(n):
        b = []
        for j in curr:
            b.append(a[i] + j)
        for j in curr:
            b.append(j - a[i])
        curr.extend(b)

    # print (curr)
    if curr.count(0)>1:
        print ("YES")
    else:
        print ("NO")

