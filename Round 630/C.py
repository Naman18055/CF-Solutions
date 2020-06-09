def check(s,k):
	string = s[0:k]
	if s==s[::-1]:
		for i in range(len(s)//k):
			if s[i*k:(i+1)*k]!=string:
				return False
		return True
	else:
		return False

def calc(s):
	options={}
	i,j,count=0,len(s)-1,0
	while i<=j:
		if s[i]!=s[j]:
			count+=1
		if i!=j:
			options[i]=[s[i],s[j]]
		else:
			options[i]=[s[i]]
		i+=1
		j-=1
	return (options,count)

for nt in range(int(input())):
	n,k=map(int,input().split())
	s=input()
	if check(s,k):
		print (0)
	else:
		freq={}
		ans=0
		for i in range(n//k):
			d,ans=calc(s[i*k:k*(i+1)])
			for j in d:
				for m in d[j]:
					if j in freq:
						if m in freq[j]:
							freq[j][m]+=1
						else:
							freq[j][m]=1
					else:
						freq[j]={m:1}
			# print (d)
			# print (ans)
		ans=0
		for i in freq:
			s=0
			m=0
			for j in freq[i]:
				s+=freq[i][j]
				if freq[i][j]>m:
					m=freq[i][j]
			ans+=s-m
		# print (freq)
		print (ans)