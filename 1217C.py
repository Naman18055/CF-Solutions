# import sys
# input = sys.stdin.readline
def calc(s):
	return int(s,2)

for nt in range(int(input())):
	s=input()
	n=len(s)
	pref=[-1]*(n)
	for i in range(n):
		if s[i]=="1":
			pref[i]=i
		else:
			pref[i]=pref[i-1]
	ans=0
	for i in range(18):
		for j in range(n-1,i-1,-1):
			temp=s[j-i:j+1]
			# print (temp,i,j,calc(temp),ans,j-pref[j-i-1])
			if calc(temp)==i+1 and temp[0]=="1":
				ans+=1
			elif s[j-i]=="1" and j-i-1>=0 and calc(temp)>i+1 and calc(temp)<=(j-pref[j-i-1]):
				ans+=1
	print (ans)