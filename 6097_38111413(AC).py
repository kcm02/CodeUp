h,w = map(int,input().split()) # 격자판 세로(h), 가로(w)
pan = [[0 for j in range(w)] for i in range(h)] # 격자판 크기 설정
n = int(input()) # 놓을 수 있는 막대의 개수

for _ in range(n): # n만큼 막대를 놓는다
    # 길이(l), 방향(d), 좌표(x,y)
    l,d,x,y = map(int,input().split())
    # ex) 3 1 2 3
    
    if bool(d): # 세로일 때, ↓
        for i in range(l):
            pan[x-1][y-1] = 1 # 좌표
            x += 1
    else:
        for i in range(l): # 가로일 때, →
            pan[x-1][y-1] = 1
            y += 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print()
