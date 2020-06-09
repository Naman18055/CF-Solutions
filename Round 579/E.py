from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
l=l.sort()
arr=[0]*150002
for i in range(n-1,-1,-1):
	if arr[l[i+1]+1]!=1:
		arr[l[i+1]+1]=1
	elif arr[l[i+1]]!=1:
		arr[l[i+1]]=1 
	else:
		if l[i+1]-1!=0:
			arr[l[i+1]-1]=1
print (sum(arr[0:l[n-1]+1]))
# cnt=defaultdict(int)
# for i in l:
# 	cnt[i]+=1
# ans=len(cnt)
# l=list(set(l))
# l.sort()
# for i in range(len(l)-1,-1,-1):
# 	if cnt[l[i]]>2:
# 		if i+1 not in cnt:
# 			cnt[i+1]+=1
# 			ans+=1
# 		if i-1 not in cnt and i-1!=0:
# 			cnt[i-1]+=1
# 			ans+=1
# 	elif cnt[l[i]]==2:
# 		if i+1 not in cnt:
# 			cnt[i+1]+=1
# 			ans+=1
# 		elif i-1 not in cnt:
# 			if i-1!=0:
# 				cnt[i-1]+=1
# 				ans+=1
# print (ans)
