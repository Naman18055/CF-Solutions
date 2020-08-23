s = input()
n = len(s)
dp = []
stack = []
ans = []
for i in range(n):
	if s[i]=="(":
		dp.append(i)
		stack.append(i)
		ans.append(i)
	else:
		if not stack:
			dp.append(-1)
			ans.append(-1)
			continue
		dp.append(stack[-1])
		if dp[-1]-1>=0 and s[dp[-1]-1]==")" and ans[dp[-1]-1]!=-1:
			ans.append(ans[dp[-1]-1])
		else:
			ans.append(dp[-1])
		stack.pop()

	# print (dp,ans)

# print (*ans)
maxx = 0
count = 1
for i in range(len(ans)):
	if i==ans[i]:
		continue
	diff = i-ans[i]+1
	if ans[i]!=-1 and diff>maxx:
		maxx = diff
		count = 1
	elif ans[i]!=-1 and diff==maxx:
		count += 1
# print (*dp)
print (maxx,count)