# 3d 토마토를 먼저 풀어서 매우 쉽게 풀린 문제네요
# 그냥 평면만 고려하면 되기에 상,하,좌,우 좌표를 이동하며 체크하면 됩니다
# 역시 처음에 모든 익은 토마토의 좌표를 큐에 넣고 BFS입니다.

import sys
from collections import deque


m,n = map(int, input().split())


tomato = []
visited = [[False for _ in range(m)] for _ in range(n)]
pos = [[1,0],[-1,0],[0,1],[0,-1]]
move = deque([])
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    tomato.append(temp)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            move.append([i,j])
            visited[i][j] = True

# BFS 시작
while move:
    x,y = move.popleft()

    for i in pos: # 저도 다음 좌표이동 문제에서는 이거 써봐야겠어요 간zi 쩌네요 -> 222
        next_step = [x+i[0], y+i[1]]
        if 0<=next_step[0] < n and 0<= next_step[1] < m:
            if visited[next_step[0]][next_step[1]] == False and tomato[next_step[0]][next_step[1]] == 0:
                move.append(next_step)
                visited[next_step[0]][next_step[1]] = True
                tomato[next_step[0]][next_step[1]] = tomato[x][y] + 1

# BFS 이후
check = 0
maxs = -2
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            check = 1
            break
        maxs = max(maxs, tomato[i][j])
    if check == 1:
        break
else:
    print(maxs-1)