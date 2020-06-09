import sys
class cell: 	
	def __init__(self, x = 0, y = 0, dist = 0): 
		self.x = x 
		self.y = y 
		self.dist = dist 
		
def isInside(x, y, N, M): 
	if (x >= 1 and x <= N and
		y >= 1 and y <= M): 
		return True
	return False
	
 
def minStepToReachTarget(knightpos, targetpos, N, M):  
	dx = [2, 2, -2, -2, 1, 1, -1, -1] 
	dy = [1, -1, 1, -1, 2, -2, 2, -2] 
	
	queue = [] 
	 
	queue.append(cell(knightpos[0], knightpos[1], 0)) 
	 
	visited = [[False for i in range(M + 1)] for j in range(N + 1)] 
	 
	visited[knightpos[0]][knightpos[1]] = True
	 
	while(len(queue) > 0): 
		
		t = queue[0] 
		queue.pop(0) 
		 
		if(t.x == targetpos[0] and
		t.y == targetpos[1]): 
			return t.dist 
			 
		for i in range(8): 
			
			x = t.x + dx[i] 
			y = t.y + dy[i] 
			
			if(isInside(x, y, N, M) and not visited[x][y]): 
				visited[x][y] = True
				queue.append(cell(x, y, t.dist + 1)) 

n,m=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
whiteknight = [x1, y1] 
whitetarget = [n//2, m//2]
blackknight = [x2, y2] 
blacktarget = [n//2+1, m//2]
ms = (minStepToReachTarget(whiteknight, blackknight, n, m))
if ms==1:
	print ("WHITE")
	print (x2,y2)
	sys.stdout.flush()
	exit(0)
wtowtarget = (minStepToReachTarget(whiteknight, whitetarget, n, m))
wtobtarget = (minStepToReachTarget(whiteknight, blacktarget, n, m))
btobtarget = (minStepToReachTarget(blackknight, blacktarget, n, m))
btowtarget = (minStepToReachTarget(blackknight, whitetarget, n, m))

if wtowtarget<=btobtarget:
	print ("WHITE")
elif wtowtarget<btowtarget:
	print ("WHITE")
elif wtobtarget-1==btobtarget:
	print ("WHITE")
else:
	print ("BLACK")

