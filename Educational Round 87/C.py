import math
t = int(input())
for i in range(t):
    s = int(input())
    if s%2:
    	print(1/(2*math.sin(math.pi/(4*s))))
    else:
    	print(1/(math.tan(math.pi/(s))))
    