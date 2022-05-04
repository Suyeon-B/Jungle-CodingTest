# 다리들 중 최솟값을 골라 더하는 부분이 막혀서 정답 참고했슴다
# bfs로 라벨링, 다리놓기 했고, MST 크루스칼로 다리 길이 최솟값 구했습니당
# 내가 생각하는 이 코드의 핵심 Key 💡
# -> 섬 라벨링 할 때 섬 좌표값을 key로 설정하면 현재 좌표만 알아도 어디 섬 위인지, 바다 위인지 알 수 있음
# 와,,,, 멋지네염
#   ㄴ2222222222
"""
모든 섬을 연결하는 다리 길이의 최솟값 구하기

조건
1. 모든 섬을 연결하는 것이 불가능하면 -1 출력
2. 다리 길이는 2 이상
3. 다리는 중간에 방향 전환 불가

IDEA
1. 우선 땅이 먼저 나오는 곳에서 bfs 탐색 시작
    'dictionary[(x, y)] = 섬의 번호' 로 저장함
2. 섬 dictionary를 bfs로 돌면서 다리를 놓음
3. 크루스칼 MST로 최소 다리 길이를 구함
"""

import sys, collections
from collections import deque
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

# 세로 크기 N과 가로 크기 M
n, m = map(int, input().strip().split())

# 섬 dictionary
islandNum = 0 # 섬의 개수 stack - dictionary key 용 / 2 ≤ 섬의 개수 ≤ 6
island = collections.defaultdict(list)
landArr = []
# 혁 ) 딕셔너리 잘쓰는 거 신기하네염 고수신가요 ?
# 지도
MAP = [list(map(int, input().strip().split())) for _ in range(n)]

# 좌표 이동용
move = [(0,1),(1,0),(0,-1),(-1,0)]

# (a, b)에서부터 bfs로 땅 찾기
def bfs_find_island(a, b):
    global islandNum
    # 방문 처리
    visited[a][b] = True
    # 큐 생성
    q = deque([(a, b)]) # 시작 값 큐에 append
    # 딕셔너리 update
    island[(a, b)] = islandNum
    landArr.append((a, b, islandNum))
    # bfs 시작
    while q:
        x, y = q.popleft() # 다음 좌표 꺼내기
        for a, b in move: # 동서남북 돌면서 땅 찾기
            nx, ny = x+a, y+b
            # 새로운 좌표가 MAP 안에 들어가고, 바다가 아니라면
            if 0<=nx<n and 0<=ny<m and MAP[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                island[(nx, ny)] = islandNum
                q.append((nx, ny))
                landArr.append((nx, ny, islandNum))


# 1. 우선 땅이 어딨나 체크해서 dictionary[땅의 번호] = 좌표들 로 저장함
visited = [[False]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if MAP[x][y] == 1 and not visited[x][y]:
            bfs_find_island(x, y)
            islandNum += 1

# 2. 섬 dictionary bfs 탐색 시작
edges = []
for x,y,curLand in landArr:
    for a,b in move: 
        dist = 0 
        nx, ny = x+a, y+b
        while True:
            if n>nx>=0 and m>ny>=0:
                toLand = island.get((nx,ny))
                # 같은 섬
                if curLand==toLand:
                    break
                # 바다 위, 다리 길이 +1
                if toLand == None:
                    nx+=a; ny+=b
                    dist+=1
                    continue
                # 다리가 짧음
                if dist < 2:
                    break
                # 다른 섬을 만나면 다리 놓기 끝
                edges.append((dist,curLand,toLand))
                break
            else:
                break
edges = sorted(edges,reverse=True)

# 크루스칼 MST 진행
def union(x,y):
    x, y = find(x), find(y)
    if x!=y:
        if x>y:
            parents[x] = y
        else:
            parents[y] = x

def find(k):
    if k == parents[k]:
        return k
    parents[k] = find(parents[k])
    return parents[k]

ans = 0
cnt = islandNum-1
parents = [i for i in range(islandNum)]
while cnt:
    try:
        w,a,b = edges.pop()
    except:
        # 저장된 다리들이 없을 때
        print(-1)
        exit(0)
    if find(a) != find(b): # 모든 섬을 연결하는 다리 길이의 최솟값
        union(a,b)
        ans += w
        cnt-=1
print(ans)


