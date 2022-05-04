import sys
import heapq
sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]
# q = deque()
q = []
min_leng = 1e9
for i in range(n):
  for j in range(m):
    if arr[i][j] == 'X':
      heapq.heappush(q, (-i, j))
      x, y = i, j
      temp = 0
      while True:
        x += 1
        if arr[x][y] == 'X':
          break
        if arr[x][y] == '#':
          min_leng = min(temp, min_leng)
          break
        temp +=1

for _ in range(len(q)):
  x, y = heapq.heappop(q)
  x *= -1
  arr[x][y] = '.'
  arr[x+min_leng][y] = 'X'

for i in range(n):    # 결과 출력
  for j in range(m):
    sys.stdout.write(arr[i][j])
  sys.stdout.write('\n')