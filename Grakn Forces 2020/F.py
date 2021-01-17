import sys
sys.setrecursionlimit(10000)

def merge(start, end):
	if (end-start)%2:
		for i in range(start, (start+end)//2):
			ans.append([i, i+(end-start)//2])
	else:
		for i in range()


def steps(start, end):
	# print ("ok",start, end)
	if start==end:
		return 
	if end==start+1:
		ans.append([start, end])
		return 
	steps(start, (start+end)//2-1)
	steps((start+end)//2, end)
	merge(start, end)



n = int(input())
ans = []
steps(0, n//2-1)
steps(n//2, n-1)
# merge(0, n//2)
print (len(ans))
for i in ans:
	print (i[0]+1, i[1]+1)

