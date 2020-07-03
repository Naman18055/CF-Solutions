from collections import Counter
n = int(input())
a = list(map(int,raw_input().split()))
c = Counter(a)
ans = 0
i = 0
while i<1010000:
	if i+1 in c:
		c[i+1] += c[i]//2
		c[i] = c[i]%2
	else:
		c[i+1] = c[i]//2
		c[i] = c[i]%2
	i += 1

# print (c)
for i in c:
	ans += c[i]

print (ans)