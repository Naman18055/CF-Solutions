t=int(input())
for nt in range(t):
	n=int(input())
	grid=[(-100000,-100000),(-100000,100000),(100000,100000),(100000,-100000)]
	for i in range(n):
		x,y,f1,f2,f3,f4=map(int,input().split())
		if f1==f2==f3==f4==1:
			continue
		else:
			if f1==1:
				if f2==1:
					if f3==1:
						grid[0]=(grid[0][0],y)
						grid[3]=(grid[3][0],y)
					else:
						if f4==1:
							grid[2]=(x,grid[2][1])
							grid[3]=(x,grid[3][1])
						else:
							grid[2]=(x,grid[2][1])
							grid[3]=(x,y)
							grid[0]=(grid[0][0],y)
				else:
					if f3==1:
						if f4==1:
							grid[1]=(grid[0][0],y)
							grid[2]=(grid[3][0],y)
						else:
							







