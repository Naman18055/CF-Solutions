ans = [1]
for i in range(2, 1001):
	k = ans[-1]+1
	while k%3==0 or str(k)[-1]=="3":
		k += 1
	ans.append(k)


for nt in range(int(input())):
	n = int(input())
	print (ans[n-1])
