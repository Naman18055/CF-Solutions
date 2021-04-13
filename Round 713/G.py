import sys
input = sys.stdin.readline

count = [0]*(10**7+1)
ans = [-1]*(10**7+1)
i = 1
while i<10**7+1:
    j = i
    while j<10**7+1:
        count[j]+=i
        j+=i
    if count[i]<10**7+1 and ans[count[i]]==-1:
        ans[count[i]] = i
    i+=1

for nt in range(int(input())):
	print(ans[int(input())])