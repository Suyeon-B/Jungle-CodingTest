# 500 * 500 * 40 => 1000만  최악의 상황을 가정했을 때, 모든 경우의 수를 탐색해도 충분한 시간
# 지옥의 빡구현.. 코드 더러움 주의
# 파이썬으로는 시간초과나고 pypy로 돌려야합니다. 그래서 그런지 메모리 엄청 잡아먹네요 ㅎ;

import sys

n, m = map(int, input().split())

num = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우 좌표값
answer = 0


def move(a, b, x, y, count):  # 해당 좌표마다 가능한 블록의 합 중 최대 값 반환하는 함수 (재귀 이용)
    if a + x >= 0 and a + x < n and b + y >= 0 and b + y < m:
        last_mov = [-x, -y]
        if count == 1:
            return 0
        else:
            temp = []
            now = num[a + x][b + y]
            for i in pos:
                if i != last_mov:
                    temp.append(move(a + x, b + y, i[0], i[1], count - 1))

            return now + max(temp)
    else:
        return 0


def move2(a, b, x, y):  # 근데 위의 함수로 ㅏ 블록이 불가능해서 ㅏ 블록용 체크하는 함수 만들었습니다
    if a + x >= 0 and a + x < n and b + y >= 0 and b + y < m:
        return num[a + x][b + y]
    else:
        return 0


# n ~ m 모든 좌표 순회하면서 해당 좌표에서 가능한 최대값을 뽑고 그 최대값 중에서 가장 큰값을 최종적으로 반환!
for i in range(n):
    temp = 0
    for j in range(m):
        max_list = 0
        other = num[i][j]
        others = []
        for l in range(4):
            next_num = move(i, j, pos[l][0], pos[l][1], 4)
            now = num[i][j]
            if next_num != 0:
                next_num += now
                max_list = max(max_list, next_num)
            other = other + move2(i, j, pos[l][0], pos[l][1])
        if i != 0 and i != n - 1 and j != 0 and j != m - 1:
            others.append(other - num[i - 1][j])
            others.append(other - num[i + 1][j])
            others.append(other - num[i][j + 1])
            others.append(other - num[i][j - 1])
            other = max(others)
        max_list = max(other, max_list)
        answer = max(answer, max_list)

print(answer)

# 와,,,개 쩌네여.,,,
# 수연) 함수로 나눠서 구현하신 거 멋집니다! 저도 빡구현 문제라도ㅎ 멋지게 풀기 노력해봐야겠어요~