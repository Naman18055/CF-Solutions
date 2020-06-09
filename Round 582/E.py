n=int(input())
s=input()
t=input()
if n>=2:
	l=["abcabc","acbacb","bacbac","bcabca","cabcab","cbacba","aabbcc","bbccaa","ccaabb","aaccbb","bbaacc","ccbbaa"]
	for i in l:
		string = ""
		if s in i or t in i:
			continue
		else:
			string = i
			break
	#print (string)
	if string=="":
		print ("NO")
	else:
		if string not in ["aabbcc","bbccaa","ccaabb","aaccbb","bbaacc","ccbbaa"]:
			temp=string[0:3]
			print ("YES")
			print (temp*n)
		else:
			first = string[0]
			second = string[2]
			third = string[4]
			print ("YES")
			print (first*n+second*n+third*n)
else:
	l=["abc","acb","bac","bca","cab","cba"]
	for i in l:
		string=""
		if s in i or t in i:
			continue
		else:
			string = i
			break
	if string=="":
		print ("NO")
	else:
		print ("YES")
		print (string)
