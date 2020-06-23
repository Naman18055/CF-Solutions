def countvowels(s):
	count = 0
	for i in s:
		if i in vowels:
			count += 1
			last = i
	return count,last


n = int(input())
a = []
count = {}
vowels = {"a",'e','i','o','u'}
last = {}
for i in range(n):
	s = input()
	d,l = countvowels(s)
	if d not in count:
		count[d] = [s]
	else:
		count[d].append(s)
	last[s] = l
lword = []
fword = []
for i in count:
	d = {}
	for j in count[i]:
		if last[j] not in d:
			d[last[j]] = j
		else:
			lword.append((j,d[last[j]]))
			del d[last[j]]
	if len(d)>1:
		k = []
		for j in d:
			k.append(d[j])
		for j in range(0,len(k)-1,2):
			fword.append((k[j],k[j+1]))
# print (lword)
# print (fword)
if len(fword)<=len(lword):
	ans = (len(fword)+(len(lword)-len(fword))//2)
	print (ans)
	for i in range(len(fword)):
		print (fword[i][0],lword[i][0])
		print (fword[i][1],lword[i][1])
	for i in range(len(fword),len(lword)-1,2):
		print (lword[i][0],lword[i+1][0])
		print (lword[i][1],lword[i+1][1])
else:
	ans = len(lword)
	print (ans)
	for i in range(ans):
		print (fword[i][0],lword[i][0])
		print (fword[i][1],lword[i][1])