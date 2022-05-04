# 유성과 땅의 최소거리를 구해서 한 번에 떨어뜨려야
# 시간 초과에서 벗어날 수 있음
# main 함수 안에 넣으면 python도 통과!
from heapq import heappop, heappush
from sys import stdin, stdout

stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

def main():
    r, s = map(int, input().strip().split())
    photo = [list(input().strip()) for _ in range(r)]

    # 유성, 땅의 좌표
    meteors = []
    min_dist = float('inf')
    for i in range(r):
        for j in range(s):
            if photo[i][j] == 'X':
                heappush(meteors, [-i, j])
                x = i
                temp = 0
                while True:
                    x += 1 # 한 칸씩 아래로 내려보며 땅과의 거리의 최솟값 구하기
                    if photo[x][j] == '#':
                        min_dist = min(temp, min_dist)
                        break
                    elif photo[x][j] == 'X':
                        break
                    temp += 1
    
    # 최소 거리만큼 유성을 떨어뜨려 배치함
    for i in range(len(meteors)):
        x, y = heappop(meteors)
        x = -x
        photo[x][y] = '.'
        photo[x+min_dist][y] = 'X'

    for i in range(r):
        stdout.write("".join(photo[i]))
        stdout.write('\n')
main()


# # 시간초과 최적화 중
# from heapq import heappop, heappush
# from sys import stdin

# stdin = open("Baekjoon/DP/input.txt",'r')
# input = stdin.readline

# def main():
#     r, s = map(int, input().strip().split())
#     photo = []
#     for i in range(r):
#         photo.append(list(input().strip().strip()))

#     # 유성, 땅의 좌표
#     stars = []
#     ground = []
#     for i in range(r):
#         for j in range(s):
#             if photo[i][j] == 'X':
#                 heappush(stars, [-i, j])
#             elif photo[i][j] == '#':
#                 ground.append([i, j])

#     # 땅과 맞닿을 때 까지 유성의 y좌표를 -1씩 내림
#     breaker = False
#     while True:
#         for _ in range(len(stars)):
#             x, y = heappop(stars)
#             x = -x
#             if [x+1, y] not in ground:
#                 photo[x][y] = '.'
#                 x += 1
#                 photo[x][y] = 'X'
#             else:
#                 breaker = True
#                 break
#         if breaker:
#             break 

#     for i in range(r):
#         print("".join(photo[i]))
# main()