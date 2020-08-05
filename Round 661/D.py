for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = []
	o,z = 0,0
	d = {}
	l = {0:{},1:{}}
	for i in range(n):
		if s[i]=="0":
			d[i] = o+1
			if o==len(ans):
				ans.append(["0"])
				l[0][o] = 1
				o += 1
			else:
				ans[o].append("0")
				z = o
				l[0][o] = 1
				if o in l[1]:
					del l[1][o]

				o = len(ans)
				for k in l[1]:
					o = k
					break
		else:
			d[i] = z+1
			if z==len(ans):
				ans.append(["1"])
				l[1][z] = 1
				z += 1
			else:
				ans[z].append("1")
				o = z
				l[1][z] = 1
				if z in l[0]:
					del l[0][z]
				z = len(ans)
				for k in l[0]:
					z = k
					break

		# print (ans,o,z,l)

	print (len(ans))
	for i in range(n):
		print (d[i],end=" ")
	print ()
