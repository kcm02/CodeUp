maze = [[int(x) for x in input().split()] for _ in range(10)] # 입력값 넣어주기
x, y = 1, 1

while True:
    if maze[x][y] == 2:  # 현재 위치에 먹이가 있는 경우
        maze[x][y] = 9
        break
    maze[x][y] = 9
    if y + 1 < 10 and maze[x][y + 1] in [0, 2]:  # 오른쪽으로 이동 가능
        y += 1
    elif x + 1 < 10 and maze[x + 1][y] in [0, 2]:  # 아래쪽으로 이동 가능
        x += 1
    else:  # 더 이상 움직일 수 없는 경우
        break

for row in maze:
    print(' '.join(map(str,row)))
