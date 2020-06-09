import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
s = []
l = []
ans = n**2
for i in range(n):
	a = list(map(int,input().split()))[1:]
	if sorted(a)[::-1]==a:
		s.append(min(a))
		l.append(max(a))
s.sort()
l.sort()
c = 0
# print (l,s)
for i in range(len(s)):
	while c<len(l) and l[c]<=s[i]:
		c += 1
	ans -= c
print (ans)