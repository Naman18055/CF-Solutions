n, m, k = map(int, input().split())
 
moves = 'U' * (n-1) + 'R' * (m-1)
for i in range(0, n):
    moves += (m - 1) * 'LR'[i % 2]
    moves += 'D'
 
print(len(moves))
print(moves)