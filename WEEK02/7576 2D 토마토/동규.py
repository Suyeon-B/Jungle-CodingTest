#문제는 이해완료
#DFS 좌표 문제 유형으로 생각함 // bfs 문제 풀이 부족에 따른..
#DFS로 생각했으나, 풀이가 진행되지 않아 답을 BFS 문제임을 파악
#BFS 문제(특) '최소일수' '주변의 토마토를 익힘'에서 파악을 했어야함 ∵ 깊이 들어갈 일이 없기 때문

import sys
from collections import deque

sys.stdin = open("input.txt")
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split()) #M: 가로칸수 N: 세로칸수

#문제에 주어진 좌표 만들기
graph = [list(map(int, input().split())) for _ in range(N)]

#입력까지는 문제 없이 완료...

que = deque([])

dx, dy =[-1, 1, 0, 0], [0, 0, -1, 1] #좌표문제의 경우 상하좌우 비교를 위해

res = 0 # 정답이 담길 변수

for i in range(N): # 1이 저장되어 있는 좌표를 찾아 que 에 저장
    for j in range(M):
        if graph[i][j] == 1:
            que.append([i,j]) 

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4): #상하좌우 돌리기 
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M  and graph[nx][ny]== 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx, ny])

bfs()
for i in graph: #행뽑기
    for j in i: #원소뽑기
        if j == 0: # bfs를 통해 다 1로 바꾼 후 안바뀐 0이 남아 있으면
            print(-1)
            exit(0) 
    res = max(res,max(i)) # 생각해내는게 어려웠다요
print(res - 1)

# 참고: https://jae04099.tistory.com/233