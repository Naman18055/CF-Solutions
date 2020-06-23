def calc(n):
	return (sum(list(map(int,list(str(n))))))

n=int(input())
ans=[]
for i in range(n-1,max(0,n-1000),-1):
	if (i+calc(i))==n:
		ans.append(i)
print (len(ans))
ans.sort()
for i in ans:
	print (i)