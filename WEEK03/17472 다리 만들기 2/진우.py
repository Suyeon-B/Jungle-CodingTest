# 각 섬들을 라벨링하고 다리 놓는거까지 구현하다, 최소 거리를 못구해서 답 참고 했습니다.
# dfs로 라벨링, bfs로 경로 계산, 크루스칼로 최단 경로 계산 했습니다.
# 코드가 좀 개판일 수 있는데 이해 안가는 부분 있으시면 말해주세요~~

import sys
from collections import deque

n,m = map(int, input().split())

maps = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

visited = [[False for _ in range(m)] for _ in range(n)]
distance = []
parents = [i for i in range(9)]

# find_parents, union_parents -> 크루스칼 쓰기 위해 작성
def find_parents(parent, a):
    if parent[a] != a:
        parent[a] = find_parents(parent, parent[a])
    return parent[a]

def union_parents(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 경로 계산 스타트
def bfs(maps, n):
    visited[n[0]][n[1]] = True
    pos= [[1,0],[-1,0],[0,1],[0,-1]]

    move = deque()
    move.append(n)
    while move:
        for _ in range(len(move)):
            my_pos = move.popleft()
            visited[my_pos[0]][my_pos[1]] = True
            for i in pos:
                nx = my_pos[0]
                ny = my_pos[1]
                count = 0
                check = 0
                while True:
                    nx += i[0]
                    ny += i[1]
                    count += 1
                    if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                        nx = my_pos[0]
                        ny = my_pos[1]
                        break
                    if maps[nx][ny] == maps[my_pos[0]][my_pos[1]]:
                        if visited[nx][ny] == False:                # 방문하지 않은 같은 섬일 경우 큐에 넣습니다.
                            move.append([nx,ny])
                        nx = my_pos[0]                              # 이미 방문한 같은섬이면 패스
                        ny = my_pos[1]
                        break
                    if maps[nx][ny] != 0:                           # 다른 섬에 도착하면 스톱
                        if count == 1:
                            nx = my_pos[0]
                            ny = my_pos[1]
                        check = 1
                        break
                if check == 1 and visited[nx][ny] == False:         # 다른 섬에 도착했고, 그 위치가 내가 방문하지 않은 경우
                    move.append([nx,ny])                            # 큐에 넣어줍니다
                    if count > 2:                                   # 다리 길이가 2 이상인 경우만 경로에 넣어줍니다
                        if (count-1, maps[my_pos[0]][my_pos[1]],maps[nx][ny]) not in distance:
                            distance.append((count-1, maps[my_pos[0]][my_pos[1]],maps[nx][ny]))

# 섬 라벨링 하는 DFS (BFS로 라벨링해도 됨 그냥 DFS가 편해서 했어요) # 수연) 고수답네요
def dfs(maps, n, label):
    
    maps[n[0]][n[1]] = label
    pos = [[1,0],[-1,0],[0,1],[0,-1]]

    for i in pos:
        ns = [n[0]+i[0], n[1]+i[1]]
        if 0<= ns[0] < len(maps) and 0<= ns[1] < len(maps[0]):
            if visited[ns[0]][ns[1]] == False and maps[ns[0]][ns[1]] == 1:
                dfs(maps, ns, label)
label = 2
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            dfs(maps, [i,j], label)
            label = label + 1

# 첫 스타트 섬 찾아주고 bfs를 통해서 경로가 나오면 크루스칼 써서 최단경로, 출력!
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0:
            bfs(maps, [i,j])
            result = 0
            distance.sort()
            for m in distance: 
                cost,x1,x2 = m

                if find_parents(parents, x1) != find_parents(parents, x2):
                    union_parents(parents, x1, x2)
                    result = result + cost
            parents_check = 0
            # 모든 섬끼리 이어질 수 없는 경우 체크
            for k in range(2, label):
                if parents[k] == k:
                    parents_check +=1
            if parents_check > 1:
                print(-1)
            else:
                print(result)
            exit(0)

