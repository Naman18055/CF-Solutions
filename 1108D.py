def color(a,b):
	if a=="R" and b=="G":
		return "B"
	elif a=="R" and b=="B":
		return "G"
	elif a=="R" and b=="R":
		return "B"
	if a=="B" and b=="G":
		return "R"
	elif a=="B" and b=="R":
		return "G"
	elif a=="B" and b=="B":
		return "R"
	if a=="G" and b=="G":
		return "R"
	elif a=="G" and b=="R":
		return "B"
	elif a=="G" and b=="B":
		return "R"

n=int(input())
s=input()
ans=str(s[0])
count=0
for i in range(1,n-1):
	if ans[-1]==s[i]:
		ans+=color(ans[-1],s[i+1])
		count+=1
	else:
		ans+=s[i]
if len(ans)!=len(s):
	if ans[-1]!=s[-1]:
		ans+=s[-1]
	else:
		ans+=color(ans[-1],s[-1])
		count+=1
print (count)
print (ans)