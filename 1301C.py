import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,m=map(int,input().split())
	z=n-m
	s=(n*(n+1))//2
	k1=z//(m+1)
	k2=z%(m+1)
	sub=((k1*(k1+1))//2)*(m+1-k2)
	sub+=(((k1+1)*(k1+2))//2)*k2
	# print (sub,k1,k2)
	print (s-sub)