pan = [[int(x) for x in input().split()] for _ in range(19)]

n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(19):
        pan[x-1][i] = int(not bool(pan[x-1][i]))
        pan[i][y-1] = int(not bool(pan[i][y-1]))

for row in pan:
    print(' '.join(map(str,row)))
