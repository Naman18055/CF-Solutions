import sys
input = sys.stdin.readline
final=""
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	d={l[0]:1}
	pref=[l[0]]
	for i in range(1,n):
		if l[i] not in d:
			d[l[i]]=1
		else:
			d[l[i]]+=1
		pref.append(pref[-1]+l[i])
	done={}
	ans=0
	for i in range(1,n):
		if pref[i] in d and pref[i] not in done:
			ans+=d[pref[i]]
			done[pref[i]]=1
	for i in range(2,n):
		for j in range(i-1):
			if pref[i]-pref[j] not in done and pref[i]-pref[j] in d:
				ans+=d[pref[i]-pref[j]]
				done[pref[i]-pref[j]]=1
				# print (pref[i]-pref[j],ans)
	final+=(str(ans)+"\n")
print (final)