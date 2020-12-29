for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if sum(a)==0:
		print ("NO")
		continue
	if sum(a)>0:
		a.sort(reverse=True)
	else:
		a.sort()
	ans = []
	c = 0
	end = []
	for i in a:
		if i!=0:
			if c+i!=0:
				ans.append(i)
				c += i
			else:
				end.append(i)
		else:
			end.append(i)
	ans.extend(end)
	print ("YES")
	print (*ans)
