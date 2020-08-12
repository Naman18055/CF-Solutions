def cover(sx,sy):
	x,y = sx,sy
	while y!=1:
		y -= 1
		ans.append((x,y))
	if sy!=m:
		y = sy
		while y!=m:
			y += 1
			ans.append((x,y))
	return [x,y]

n,m,sx,sy = map(int,input().split())
x,y = sx,sy
ans = []
end = [sx+1,sy]
while len(ans)<n*m:
	while end!=[1,1] and end!=[1,m]:
		end[0] -= 1
		ans.append(end)
		end = cover(end[0],end[1])
		# print (ans,end)
	end = [sx,end[1]]
	while end!=[n,1] and end!=[n,m]:
		end[0] += 1
		ans.append(end)
		end = cover(end[0],end[1])
		# print (ans,end)
for i in ans:
	print (i[0],i[1])