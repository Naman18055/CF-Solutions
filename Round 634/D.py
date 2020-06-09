# import sys
# input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	matrix=[]
	for i in range(9):
		s=input()
		# print (s)
		matrix.append(list(s))
	# for i in range(9):
	# 	for j in range(9):
	# 		print (matrix[i][j],end="")
	# 	print ()
	ans=[[-1 for i in range(9)] for j in range(9)]
	for i in range(9):
		for j in range(9):
			if j==((i%3)*3+(i//3)):
				# print (i,j)
				if i%3==0:
					ans[i][j]=matrix[i+1][j]
				else:
					ans[i][j]=matrix[i-1][j]
			else:
				ans[i][j]=matrix[i][j]
	for i in range(9):
		for j in range(9):
			print (ans[i][j],end="")
		print ()


