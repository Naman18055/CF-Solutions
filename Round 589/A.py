def calc(i):
	l=list(i)
	if len(set(l))==len(l):
		return True
	else:
		return False
l,r=map(int,input().split())
for i in range(l,r+1):
	if calc(str(i)):
		print (i)
		exit(0)
print (-1)