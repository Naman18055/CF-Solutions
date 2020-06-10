n = int(input())
s = input()
a,b = 0,0
q1,q2 = [],[]
for i in range(n//2):
	if s[i]!="?":
		a += int(s[i])
	else:
		q1.append(i)
	if s[n-i-1]!="?":
		b += int(s[n-i-1])
	else:
		q2.append(n-i-1)
a += len(q1)//2*9
b += len(q2)//2*9
if a==b:
	print ("Bicarp")
else:
	print ("Monocarp")


