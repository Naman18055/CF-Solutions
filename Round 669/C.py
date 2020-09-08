import sys

def askquery(i,j):
	print ("?",i,j)
	sys.stdout.flush()
	return int(input())

n = int(input())
ans = [0]*n
curr = 1
i = 2
count = n
while count != 1:
	a = askquery(curr,i)
	b = askquery(i,curr)
	if a>b:
		ans[curr-1] = a
		while ans[curr-1]!=0:
			curr += 1
	else:
		ans[i-1] = b
		i += 1
	while i<=curr:
		i += 1
	count -= 1

# print (ans)
left = (n*(n+1))//2 - sum(ans)
for i in range(n):
	if not ans[i]:
		ans[i] = left
		break
print ("!",*ans)