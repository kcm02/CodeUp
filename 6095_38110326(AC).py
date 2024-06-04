n = int(input())
badukpan = [[0 for j in range(19)] for i in range(19)]

for i in range(n):
    x, y = map(int,input().split())
    badukpan[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(badukpan[i][j], end=' ')
    print()
