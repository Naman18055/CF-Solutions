def calc(a,b,c):
	if a=="a":
		if c!="b":
			return "b"
		else:
			return "c"
	else:
		if a=="b":
			if c=="c":
				return "a"
			else:
				return "c"
		else:
			if c!="a":
				return "a"
			else:
				return "b"

t=int(input())
for nt in range(t):
	s=input()
	ans=""
	if len(s)==1:
		if s[0]=="?":
			print ("a")
		else:
			print (s)
		continue
	flag=0
	for i in range(len(s)-1):
		if s[i]==s[i+1] and s[i]!="?":
			print (-1)
			flag=1
			break
	if flag==1:
		continue
	if s[0]=="?":
		if s[1]=="a":
			ans+="b"
		else:
			ans+="a"
	else:
		ans+=s[0]
	for i in range(1,len(s)-1):
		if s[i]=="?":
			ans+=calc(ans[-1],"?",s[i+1])
		else:
			ans+=s[i]
	if s[-1]=="?":
		if ans[-1]=="a":
			ans+="b"
		else:
			ans+="a"
	else:
		ans+=s[-1]
	print (ans)