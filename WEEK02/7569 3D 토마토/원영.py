"""
2차원 토마토를 풀고 이해했다면 충분히 풀 수 있는 문제
z축을 생각해서 BFS를 돌리면 된다.
"""
# 원영씨 시간 메모리 얼마나 걸렸는지도 남겨주세요^_^ 하잇
from collections import deque
import sys

sys.stdin = open("input.txt",'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs():
  while q:
    z, x, y = q.popleft()
    for i in range(4):
      nx = x+ dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0<= ny <m and tomato[z][nx][ny] == 0:
        tomato[z][nx][ny] = tomato[z][x][y] +1
        q.append((z,nx,ny))
    # 혁) 이거 신박하네요
    for j in range(2): # 수연) 오 이렇게 층만 바꿔서 다시 돌려봐야겠다 나도
      nz = z+ dz[j]
      if 0<= nz <h and tomato[nz][x][y] == 0:
        tomato[nz][x][y] = tomato[z][x][y] +1
        q.append((nz,x,y))


m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
  tomato.append([list(map(int, input().split())) for _ in range(n)])

dx = [1,-1,0,0]
dy = [0,0, 1,-1]
dz = [-1, 1]
q= deque([])
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k] == 1:
        q.append((i,j,k))

bfs()
max_day = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k] == 0:
        print(-1)
        exit(0)
      max_day = max(tomato[i][j][k], max_day)

print(max_day-1)




# 잘 보고 갑니다. 논리 구조는 비슷한데 뭔가 코드가 깔끔해 보이네요