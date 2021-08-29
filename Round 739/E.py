# def check(i, j, t, done):
# 	while i<n and j<len(t):
# 		# print (s[i], t[j])
# 		if t[j] in done:
# 			j += 1
# 			continue

# 		if s[i]!=t[j]:
# 			return False
# 		i += 1
# 		j += 1
# 	while j<len(t) and t[j] in done:
# 		j += 1
# 	# print (i, j)
# 	if j==len(t):
# 		return i
# 	return False


# def found(t):
# 	ans = ""
# 	i, j = len(t), 0
# 	done = {}
# 	while i<n:
# 		if j==len(t):
# 			j = 0
# 			# break
# 		here = False
# 		if t[j] in done:
# 			j += 1
# 			continue

# 		# print (i, j, s[i:], t[j])
# 		if s[i]==t[j]:
# 			i += 1
# 			j += 1
# 		else:
# 			done[t[j]] = 1
# 			# print (t, i, j, done)
# 			p = check(i, j, t, done)
# 			if not p or p==i:
# 				return False
# 			ans += t[j]
# 			i = p
# 			j = 0
# 			here = True

# 		if here and j!=0:
# 			while j<len(t) and t[j] in done:
# 				j += 1
# 			if j!=len(t):
# 				done[t[j]] = 1
# 				ans += t[j]
# 				j = 0

# 		if i==n and not here:
# 			while j<len(t) and t[j] in done:
# 				j += 1
# 			if j!=len(t):
# 				done[t[j]] = 1
# 				ans += t[j]
# 				j = 0

# 	# print (done)
# 	for i in t:
# 		if i not in done:
# 			ans += i
# 			done[i] = 1
# 			break
# 	if len(done)!=diff:
# 		return False

# 	return ans

def checkfinal(final):
	t = final
	ans = t
	done = {}
	for i in order:
		done[i] = 1
		for j in t:
			if j not in done:
				ans += j
	if ans!=s:
		return False
	return True

def check(t):
	ans = t
	done = 0
	for i in order:
		done += count[i]
		ans += (t-done)
	if ans!=n:
		return False
	return True





# for nt in range(int(input())):
# 	s = input()
# 	diff = len(set(s))
# 	n = len(s)
# 	done = False
# 	for i in range(1, n+1):
# 		ans = found(s[0:i])
# 		if ans:
# 			final = [s[0:i], ans]
# 			if checkfinal(final):
# 				done = True
# 				print (final[0], final[1])
# 				break

# 	if not done:
# 		print (-1)
# 		continue

for nt in range(int(input())):
	s = input()
	diff = len(set(s))
	n = len(s)
	done = {}
	order = ""
	for i in range(n-1, -1, -1):
		if s[i] not in done:
			order += s[i]
			done[s[i]] = 1
	order = order[::-1]

	found = True
	count = {}
	for i in s:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1

	ans = {}
	length = 0
	for i in range(diff):
		if count[order[i]]%(i+1)!=0:
			found = False
			break
		ans[order[i]] = count[order[i]]//(i+1)
		length += count[order[i]]//(i+1)

	if found:
		res = s[0:length]
		if not checkfinal(res):
			found = False


	if not found:
		print (-1)
	else:

		print (res, order)



























