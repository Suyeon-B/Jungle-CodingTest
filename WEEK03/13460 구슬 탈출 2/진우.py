# 첫 접근 방식 -> 빨간공 먼저 굴리고, 파란공 굴리고 하는 방법으로 접근했습니다.
# 동시에 굴려지는걸 구현을 잘 못하겠어서 따로 구현했더니 예외사항이 발생했음 (같은 코스트로 R,B가 O에 들어갈때)
# 오래 고민하다가 결국 답 참고했습니다. 고슴도치랑 좀 비슷했던거 같기도 하고 연습이 필요하네요

import sys
from collections import deque

n,m = map(int, input().split())

maps=[]
red = 0
blue = 0
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    maps.append(temp)
    if 'R' in temp:
        red=[i, temp.index('R')]
    if 'B' in temp:
        blue=[i, temp.index('B')]


def solved(rx,ry,bx,by):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    move = deque()
    visited = []
    move.append((rx,ry,bx,by))
    visited.append((rx,ry,bx,by))
    count = 0
    while True:
        if count > 10:
                print(-1)
                return
        for _ in range(len(move)):
            red_x,red_y,blue_x,blue_y = move.popleft()
            if maps[red_x][red_y] == 'O':
                    print(count)
                    return
            for i in range(4):
                nred_x = red_x
                nred_y = red_y
                while True:
                    nred_x += dx[i]
                    nred_y += dy[i]
                    if maps[nred_x][nred_y] == '#':
                        nred_x -= dx[i]
                        nred_y -= dy[i]
                        break
                    if maps[nred_x][nred_y] == 'O':
                        break
                nblue_x = blue_x
                nblue_y = blue_y
                while True:
                    nblue_x += dx[i]
                    nblue_y += dy[i]
                    if maps[nblue_x][nblue_y] == '#':
                        nblue_x -= dx[i]
                        nblue_y -= dy[i]
                        break
                    if maps[nblue_x][nblue_y] == 'O':
                        break
                if maps[nblue_x][nblue_y] == 'O':
                    continue
                if nred_x == nblue_x and nred_y == nblue_y:
                    if abs(nred_x-red_x) + abs(nred_y-red_y) > abs(nblue_x-blue_x) + abs(nblue_y-blue_y):
                        nred_x -= dx[i]
                        nred_y -= dy[i]
                    else:
                        nblue_x -= dx[i]
                        nblue_y -= dy[i]
                if (nred_x,nred_y,nblue_x,nblue_y) not in visited:
                    move.append((nred_x,nred_y,nblue_x,nblue_y))
                    visited.append((nred_x,nred_y,nblue_x,nblue_y))
        count = count+1

solved(red[0],red[1],blue[0],blue[1])
# 혁) visited 쓰는 방식이 제가 가져온 코드랑 조금 다르긴한데 뀨) 신가하네요
# 진우님은 왜 4차원 배열을 써야 돌아가는지 이유 아시나요 ?!
# 아시면 내일 공유 부탁드려요 !!

# 4차원 배열을 쓰나요.....??? 다 2차원 같은데