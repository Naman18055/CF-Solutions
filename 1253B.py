n = int(input())
a = list(map(int,input().split()))
count = 0
e,l = {},{}
ans = []
for i in a:
	if i>0 and i in e:
		count = -1
		break
	elif i>0:
		e[i] = 1
		count += 1
	elif i in l:
		count = -1
		break
	else:
		if -1*i not in e:
			count = -1
			break
		l[i] = 1
		count += 1
	if len(e)==len(l):
		e,l = {},{}
		ans.append(count)
		count = 0
if len(e)!=len(l):
	print (-1)
	exit()
if count == -1:
	print (-1)
	exit()
print (len(ans))
print (*ans)