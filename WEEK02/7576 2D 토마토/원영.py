"""
토마토가 익어가는게 넓게 퍼져나가기에 BFS를 써야한다 생각함
토마토가 하나가 있을 때 걸리는 날짜는 계산이되었는데 2개가 있을 때를 어떻게 해야할지 몰라서 답봄
q의 특성을 이용해서 시작하는 지점을 모두 q에 넣고 시작하면 2개가 있을 때도 가능
"""
from collections import deque
import sys
sys.stdin = open("input_py.txt") # 수연) 스승님 덕분에 야무지게 잘 쓰고 있슴다
input = sys.stdin.readline
q = deque([])
def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y +dy[i]
      # if 0 > nx or nx>= n or ny>0 or ny <= m :
      #   continue
      if 0<= nx < n and 0<= ny < m and tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y] +1
        q.append((nx,ny))

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0,0]
dy = [0,0, 1, -1]

total_day = 0
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      q.append((i,j)) # 수연) 튜플, 리스트 모두 사용해도 되는데, 좌표값같은 변하지 않는 데이터에 한해서는 튜플이 리스트보다 메모리도 적게 쓰고 속도도 빠르대요! 덕분에 튜플 장점 배워감니다 -> 오호,,,, 손가락 복잡도만 낮을줄 알았는데 그런 장점이 .... 
bfs()
for i in tomato:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  total_day = max(total_day,max(i))

print(total_day-1)


# 잘 보고 갑니다~~ 💩