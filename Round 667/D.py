def calc(n):
	ans = 0
	for i in n:
		ans += int(i)
	return ans

for nt in range(int(input())):
	n,s = input().split()
	s = int(s)
	f = calc(n)
	if f<=s:
		print (0)
		continue
	n = n[::-1]
	if n[0]=="0":
		ans = [0]
		flag = 0
		diff = f-s
	else:
		ans = [10-int(n[0])]
		flag = 1
		diff = f-s-int(n[0])

	# print (n)
	for i in range(1,len(n)):
		x = int(n[i])
		if flag:
			x += 1
			diff += 1
		if diff<=0:
			break
		# print (i,x,diff)

		if x==0:
			flag = 0
			diff -= int(n[i])
			ans.append(0)
			continue

		flag = 1
		ans.append(10-x)
		diff -= x

	new = []
	flag = 0
	for i in ans[::-1]:
		if i!=0 or (i==0 and flag):
			flag = 1
			new.append(i)
		else:
			continue


	print ("".join(map(str,new)))