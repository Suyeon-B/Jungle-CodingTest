# 정상 동작하지 않는 코드 입니다. 수정 포기 리스트로 구현하다 포기했습니다.
from collections import deque
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def numbering(x,y,number):
  q = deque([(x,y)])
  while q:
    x, y = q.popleft()
    jejudo[x][y] = number 
    jejudolist.append((x,y,number))
    visited[x][y] = True

    for i in range(4):
      nx = x+ dx[i]
      ny = y + dy[i]
      if 0<= nx < n and 0<= ny <m and jejudo[nx][ny] == 1 and not visited[nx][ny]:
        q.append((nx,ny))

def bild_bridge(bridge):
  for x,y, land_num in jejudolist:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dist = 0
      while True:
        if 0<= nx < n and 0 <= ny <m:
          if land_num == jejudo[nx][ny]:
            break

          if jejudo[nx][ny] == 0:
            dist+=1
            nx += dx[i]
            ny += dy[i]
            continue
          if dist <2:
            break
          bridge.append((dist, land_num, jejudo[nx][ny]))
          break
        else:
          break
  return

dx = [1,-1,0,0]
dy= [0,0,1,-1]

n, m = map(int, input().split())
jejudo = [list(map(int, input().split())) for _ in range(n)]
visited =[[False]*m for _ in range(n)]
jejudolist = []

number = 1
for i in range(n):
  for j in range(m):
    if jejudo[i][j] == 1 and not visited[i][j]:
      numbering(i,j, number)
      number += 1

bridge = []
bild_bridge(bridge)
bridge = sorted(bridge, reverse=True)
print(bridge)

def find(a):
  if a != parents[a]:
    a = find(parents[a])
  return parents[a]

def union(a,b):
  a = find(a)
  b = find(b)

  parents[b] = a

parents = [i for i in range(number)]
answer = 0
cnt = number -1
while cnt:
  try:
    w,a,b = bridge.pop()
  except:
    print(-1)
    exit(0)
  
  if find(a) != find(b):
    union(a,b)
    answer += w
    cnt -=1

print(answer)
