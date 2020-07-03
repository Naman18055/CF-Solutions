from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a2 = len(set(a))
c = Counter(a)
a1 = 0
for i in c:
	a1 = max(a1,c[i])
print (a1,a2)