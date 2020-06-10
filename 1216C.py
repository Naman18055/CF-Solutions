def calc(x,y,b):
	x1,y1,x2,y2 = b
	return x<x1 or x2<x or y<y1 or y>y2

w = list(map(int,input().split()))
b1 = list(map(int,input().split()))
b2 = list(map(int,input().split()))
for i in range(4):
	w[i] *= 2
	b1[i] *= 2
	b2[i] *= 2
ans = "NO"
for i in range(w[0],w[2]+1):
	if calc(i,w[1],b1) and calc(i,w[1],b2):
		ans = "YES"
		break
	if calc(i,w[3],b2) and calc(i,w[3],b1):
		ans = "YES"
		break
if ans=="YES":
	print (ans)
	exit()
for i in range(w[1],w[3]+1):
	if calc(w[0],i,b1) and calc(w[0],i,b2):
		ans = "YES"
		break
	if calc(w[2],i,b2) and calc(w[2],i,b1):
		ans = "YES"
		break
print (ans)