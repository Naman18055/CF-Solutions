for nt in range(int(input())):
    n, k = map(int,input().split())
    m = n
    while len(set(str(n))) > k:
        if n%10==0:
            n = n//10
        else:
            n += 1
    end = str(min(str(n))) * (len(str(m))-len(str(n)))
    print (int(str(n)+end))