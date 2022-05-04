######## 고친 나만의 CODE .... 3시간 걸림... 푼사람들 존경합니다
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

R, S = map(int, input().split())

pixels = [[x for x in input().strip()] for _ in range(R)]

minDistance = 3000

for y in range(S):
    meteor = -1
    for x in range(R):
        if pixels[x][y] == "X":
            meteor = max(meteor, x)
        if pixels[x][y] == "#" and meteor >= 0:
            minDistance = min(minDistance, x-meteor-1)
            break
if minDistance == 0:
    for i in range(R):
        print(*pixels[i], sep='')
        sys.exit(0)

for x in range(R-1, -1, -1):
    for y in range(S):
        if pixels[x][y] == "X":
            pixels[x][y] = "."
            pixels[x+minDistance][y] = "X"

for i in range(R):
    print(*pixels[i], sep='')


################ 오답 코드
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

R, S = map(int, input().split())

pixels = [[x for x in input().strip()] for _ in range(R)]

# 인덱스별 제일 높은 땅의 위치랑
# 인덱스별 제일 낮은 유성의 위치가 1차이나는지

# 제일 밑에 있는 유성의 위치 찾아
# 그 열 .(count)만큼 다 빼
# 다른 줄도 count만큼 . 없애


def findMeteor():
    lastX = 0
    lastY = 0
    for i in range(R):
        for j in range(S):
            if pixels[i][j] == "X":
                lastX = i
                lastY = j
    return [lastX, lastY]


def findEarth(x, y):
    for i in range(x+1, R):
        if pixels[i][y] == "#":
            return i-x-1


# 유성의 좌표
coordinate = findMeteor()
# 유성과 땅의 차이
count = findEarth(coordinate[0], coordinate[1])
print(f"count : {count}")
# [i][j] swap [i+count][j]
for i in range(coordinate[0]):
    for j in range(S):
        if pixels[i][j] == "X":
            pixels[i][j], pixels[i+count][j] = pixels[i+count][j], pixels[i][j]

for i in range(R):
    print(*pixels[i], sep='')

################ 오답 코드
# 땅과 유성의 최소 차이를 구해야하는데 잘못생각함
################ 정답 코드
import sys
input = sys.stdin.readline
 
R, S = map(int, input().split())
meteor = [input() for _ in range(R)]    # 유성 충돌 전
arr = [['.'] * S for _ in range(R)]    # 유성 충돌 후
 
move = 1 << 14    # 유성이 최종적으로 움직여야하는 거리
 
for x in range(S):
    temp_meteor = 0    # 가장 높은 유성 행 좌표 (좌표가 높아야 땅과의 거리가 가깝다.)
    temp_ground = 9999    # 가장 낮은 땅 행 좌표 (좌표가 낮아야 유성과의 거리가 가깝다.)
    flag = False    
    for y in range(R):
        if meteor[y][x] == 'X':
            temp_meteor = max(temp_meteor, y)
            flag = True    # 유성이 있는 좌표를 만나면 True
        elif meteor[y][x] == '#':
            temp_ground = min(temp_ground, y)
    if flag:    # 유성이 있는 좌표에서 `move` 계산
        move = min(abs(temp_meteor-temp_ground)-1, move)
 
for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X':
            arr[x+move][y] = 'X'    # 유성을 최종 move만큼 움직인다.
        if meteor[x][y] == '#':
            arr[x][y] = '#'
 
for i in range(R):    # 결과 출력
    for j in range(S):
        sys.stdout.write(arr[i][j])
    sys.stdout.write('\n')

