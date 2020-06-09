def calc(n,r):
	return ((fact[n])//(fact[r]*fact[n-r]))

def ans(a):
	a=str(a)[::-1]
	answer=0
	for i in range(len(a)):
		if (int(a[i]))!=0:
			# print (int(a),i,17)
			answer+=(limit[int(a[i])-1][17-i])
	return answer

limit=[[0 for i in range(18)] for j in range(10)]
fact=[1,1]
for i in range(2,20):
	fact.append(fact[-1]*i)
for i in range(17,-1,-1):
	for j in range(10):
		if i>=15:
			limit[j][i]=0
			continue
		for k in range(i+1,18):
			limit[j][i]+=limit[9][k]*calc(18-i,18-k)
		limit[j][i]+=(j)*9*8*7*(6**(14-i))
# for i in limit:
# 	print (*i)

for nt in range(int(input())):
	a,b=map(int,input().split())
	if a==1:
		print (ans(b))
	else:
		print ((ans(b))-ans(a-1))
