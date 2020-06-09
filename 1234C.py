for nt in range(int(input())):
	n=int(input())
	dp=[]
	dp.append(input())
	dp.append(input())
	curr=[1,1]
	prev=0
	while True:
		if int(dp[curr[0]-1][curr[1]-1])<=2:
			if prev==1:
				flag=0
				break
			curr=[curr[0],curr[1]+1]
			prev=0
		else:
			if prev==0:
				if curr[0]==1:
					curr=[curr[0]+1,curr[1]]
				else:
					curr=[curr[0]-1,curr[1]]
				prev=1
			elif prev==1:
				curr=[curr[0],curr[1]+1]
				prev=0

		# print (curr,prev)
		if curr[0]==2 and curr[1]==n+1:
			flag=1
			break
		if curr[0]>2 or curr[1]>n:
			flag=0
			break
		
	if flag:
		print ("YES")
	else:
		print ("NO")