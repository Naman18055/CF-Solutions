s = list(map(int,input().split()))
d = {"S":s[0],"M":s[1],"L":s[2],"XL":s[3],"XXL":s[4],"XXXL":s[5]}
o = {0:"S",1:"M",2:"L",3:"XL",4:"XXL",5:"XXXL"}
n = int(input())
l = []
for i in range(n):
	s = input()
	if "," not in s:
		l.append(s.split())
	else:
		l.append(s.split(","))
flag = 0
done = {}
for i in range(n):
	if len(l[i])==1:
		if d[l[i][0]]==0:
			flag = 1
			break
		else:
			d[l[i][0]] -= 1
			done[i] = l[i][0]
if flag:
	print ("NO")
	exit()
for i in range(6):
	if i==0:
		j = 0
		while d[o[i]]!=0 and j<n:
			if j not in done and o[i] in l[j] and o[i+1] in l[j]:
				done[j] = o[i]
				d[o[i]] -= 1
			j += 1
	else:
		j = 0
		while d[o[i]]!=0 and j<n:
			if j not in done and o[i] in l[j] and o[i-1] in l[j]:
				done[j] = o[i]
				d[o[i]] -= 1
			j += 1
		j = 0
		while d[o[i]]!=0 and j<n:
			if j not in done and o[i] in l[j] and o[i+1] in l[j]:
				done[j] = o[i]
				d[o[i]] -= 1
			j += 1
if len(done)!=n:
	print ("NO")
else:
	print ("YES")
	for i in range(n):
		print (done[i])

