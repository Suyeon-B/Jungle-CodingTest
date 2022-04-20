# 모두들 빡구현을 하셨길래 !
# 저는 좋은 dfs코드를 가져와 보았습니다 ^_^
# (사실 못풀겠어요 ...)
import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    # if idx == 3) 4개 방문한거니 최대값 구하기
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            # move r -> nr // c -> nc
            nr = r + dr[i]
            nc = c + dc[i]
            # nr, nc가 arr에 속해있는지, 방문한건지 확인
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 빠큐모양
                if idx == 1:
                    visit[nr][nc] = 1
                    # nr, nc를 방문처리하지만 (r,c)에 머물러 있음
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                #######################
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 0이면 방문안한것
visit = [([0] * M) for _ in range(N)]
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

# 수연) 나도 이거 dfs로 어떻게 푸는지 궁금하다!!! 이거 혹시 내일 dfs 방식으로 설명 가능하신지?