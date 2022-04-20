# 답봤습니다.
# 근데 visited를 빨강, 파랑 따로 만들어서 체크하려고하니 오답이 나오고
# 4차원 배열에 같이 확인하니 정답이 나오네요 왜이러는지 이유를 모르겠네요
# 구현 문제는 확실히 손가락 복잡도가 높고 시간이 많이 걸리는 것 같습니다.
# 혁) 나도 4차원-> 3차원으로 고쳐서 체크 해봤는데 오답이 나와요 이유는 모르겠어요
from collections import deque
import sys
sys.stdin = open("input_py.txt", "r")

n, m = map(int ,input().split())
board = [list(input().strip()) for _ in range(n)]
# red_board = [[False]*m for _ in range(n)]
# blue_board = [[False]*m for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

q = deque()
def init():
  for i in range(n):
    for j in range(m):
      if board[i][j] == 'R':
        rx, ry = i,j
      if board[i][j] == 'B':
        bx, by = i,j
  # 각 구슬 좌표 및 움직임 카운트
  q.append((rx,ry,bx,by,1))
  visited[rx][ry][bx][by] = True
  # red_board[rx][ry] = True
  # blue_board[bx][by] = True

def move(x, y, dx, dy):
  cnt = 0
  while board[x+dx][y+dy] != '#' and board[x][y] !='O':
    x += dx
    y += dy
    cnt +=1
  return x,y, cnt

def bfs():
  init()
  dx =[ 1, -1, 0, 0]
  dy =[ 0, 0, 1, -1]

  while q:
    rx, ry, bx, by, mcnt = q.popleft()
    if mcnt > 10:
      break
    for i in range(4):
      nrx, nry, rcnt = move(rx,ry, dx[i], dy[i])
      nbx, nby, bcnt = move(bx,by, dx[i], dy[i])
      if board[nbx][nby] != 'O':
        if board[nrx][nry] =='O':
          print(mcnt)
          return
      
        if nrx == nbx and nry == nby:
          if rcnt > bcnt:
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        if not visited[nrx][nry][nbx][nby]:
          visited[nrx][nry][nbx][nby] = True
        # if not red_board[nrx][nry] and not blue_board[nbx][nby]:
        #   red_board[nrx][nry] = True
        #   blue_board[nbx][nby] = True
          q.append((nrx,nry,nbx,nby, mcnt+1))
  
  print(-1)

bfs()