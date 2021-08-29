import sys
input = sys.stdin.readline

def compare(a, b): # a to b by deleting/adding to right
	ans = 0
	j = 0
	for i in range(len(a)):
		if j==len(b):
			return ans + len(a)-i
		if a[i]==b[j]:
			j += 1
		else:
			ans += 1
	return ans + len(b)-j


powers = [1]
for i in range(60):
	powers.append(powers[-1]*2)

for nt in range(int(input())):
	n = int(input())
	ans = 100
	for i in powers:
		ans = min(ans, compare(str(n), str(i)))
	print (ans)