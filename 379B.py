n=int(input())
l=list(map(int,input().split()))
ans=""
s=sum(l)
i=0
while s!=0 and i<n:
	if l[i]!=0 and i<n-1:
		ans+="P"
		ans+="R"
		ans+="L"
		l[i]-=1
		s-=1
	elif l[i]!=0 and i==n-1:
		ans+="P"
		ans+="L"
		ans+="R"
		l[i]-=1
		s-=1
	elif l[i]==0:
		ans+="R"
		i+=1
print (ans)