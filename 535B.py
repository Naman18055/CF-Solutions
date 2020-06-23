n = int(input())
if n==4:
	print (1)
	exit()
b = len(str(n))
a = []
a.append("4")
a.append("7")
k = 0
l = {"4":0,"7":1}
while a[-1]!=str(n):
	if "4" not in a[-1]:
		a.append("4"*(len(a[-1])+1))
		l[a[-1]] = len(a)-1
		j = l["4"*len(a[-2])]+1
		k = 0
	elif "4" not in a[-1][1:]:
		k += 1
		a.append(a[k]+"4"*(len(a[-1])-1))
		l[a[-1]] = len(a)-1
		j = l["4"*(len(a[-1])-1)]+1
	else:
		a.append(a[k]+a[j])
		l[a[-1]] = len(a)-1
		j += 1
	# print (a,l)
# print (a)
print (len(a))