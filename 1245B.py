import math
for nt in range(int(input())):
	n = int(input())
	a,b,c = map(int,input().split())
	s = input()
	ans = ""
	for i in s:
		if i=="R":
			if b>0:
				b-=1
				ans+="P"
			else:
				ans+="A"
		if i=="P":
			if c>0:
				c-=1
				ans+="S"
			else:
				ans+="A"
		if i=="S":
			if a>0:
				a-=1
				ans+="R"
			else:
				ans+="A"
	if len(ans)-ans.count("A")>=math.ceil(n/2):
		print ("YES")
		f = ""
		for i in ans:
			if i!="A":
				f += i
			else:
				if a>0:
					a-=1
					f+="R"
				elif b>0:
					b-=1
					f+="P"
				else:
					c-=1
					f+="S"
		print (f)
	else:
		print ("NO")