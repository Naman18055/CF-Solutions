n = int(input())
ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
bx,cx = max(bx,cx),min(bx,cx)
by,cy = max(by,cy),min(by,cy)
if (ax<=bx and ax>=cx) or (ay>=cy and ay<=by):
	print ("NO")
else:
	print ("YES")