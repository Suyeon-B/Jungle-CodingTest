# 처음에 모든 익은 토마토의 좌표를 큐에 넣고
# BFS를 돌립니다.
# 밑에 next_step 있는게 좀 복잡해 보일 수 있는데, 그냥 평면 상,하,좌,우 입체 상,하 를 고려하는 if문 입니다~

import sys
from collections import deque


m,n,h = map(int, input().split())

tomato = []

for i in range(h):
    temp = []
    for j in range(n):
        temp2 = list(map(int, sys.stdin.readline().split()))
        temp.append(temp2)
    tomato.append(temp)


pos = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]] # 수연) 동,서,남,북,아래,위를 한번에 담아서 좋은 것 같아요!

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

move = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                move.append([i,j,k])
                visited[i][j][k] = True

# BFS 시작
while move:
    height, col, row = move.popleft()
    # 혁) 모두 while문 안에 for문을 썼는데 왜 이렇게 시간 차이가 많이 날까요 ?
    for i in pos: # 수연) 와 확실히 for문 하나로 돌리니까 시간복잡도 압살하셨네여
        next_step = [height+i[0], col+i[1], row+i[2]]
        if 0<= next_step[0] < h and 0<= next_step[1] < n and 0<= next_step[2] < m:
            if visited[next_step[0]][next_step[1]][next_step[2]] == False and tomato[next_step[0]][next_step[1]][next_step[2]] == 0:
                move.append([next_step[0], next_step[1], next_step[2]])
                visited[next_step[0]][next_step[1]][next_step[2]] = True
                if tomato[next_step[0]][next_step[1]][next_step[2]] == 0 and tomato[height][col][row] >= 1:
                    tomato[next_step[0]][next_step[1]][next_step[2]] = tomato[height][col][row] + 1

# BFS 이후
check = 0
maxs= -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                check = 1 # 수연) check 변수 없애고 여기서 exit(0) 하면 될 것 같아요!
                print(-1)
                break
            maxs = max(maxs, tomato[i][j][k])
        if check == 1: 
            break
    if check == 1:
        break
else:
    print(maxs-1)