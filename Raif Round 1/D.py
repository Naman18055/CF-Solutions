n = int(input())
a = list(map(int,input().split()))
o = []
pair = []
chain = []
f = True
extra = 0
three, two = False, False
for i in range(n-1,-1,-1):
	if a[i]==0:
		continue
	if a[i]==1:
		o.append(i)
	elif a[i]==2:
		two = True
		if not o:
			f = False
			break
		else:
			pair.append((i,o.pop()))
	else:
		if three:
			chain.append(i)
		elif two:
			chain.append(pair[-1][0])
			chain.append(i)
		else:
			if not o:
				f = False
			else:
				chain.append(o.pop())
				chain.append(i)
				extra = 1
		three = True
if not f:
	print (-1)
	exit()
chain = chain[::-1]

# print (pair)
# print (chain)

ans = []
done = set(chain)
r = 1
for i in range(len(chain)-1):
	ans.append((r, chain[i]+1))
	ans.append((r, chain[i+1]+1))
	r += 1
if extra:
	ans.append((r, chain[-1]+1))
	r += 1

for i in pair:
	ans.append((r, i[0]+1))
	ans.append((r, i[1]+1))
	done.add(i[0])
	done.add(i[1])
	r += 1

for i in range(n):
	if a[i]==1 and i not in done:
		ans.append((r, i+1))
		r += 1

print (len(ans))
for i in ans:
	print (i[0], i[1])






