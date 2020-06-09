
def mult_input():
	return map(int,input().split())
 
def list_input():
	return list(map(int,input().split()))
 
# prime=[[1] for i in range(101)]
# for i in range(2,101):
# 	for j in range(i,101,i):
# 		prime[j].append(i)
# print (prime)
for nt in range(int(input())):
	n=int(input())
	l=list_input()
	if n==1:
		print (1)
		continue
	ans=[1]*(n+1)
	for i in range(1,n+1):
		j=2*i
		while j<=n:
			if l[j-1]>l[i-1]:
				ans[j-1]=max(ans[j-1],ans[i-1]+1)
			j+=i
		# print (ans)
	final=0
	# print (ans)
	for i in ans:
		final=max(i,final)
	print (final)