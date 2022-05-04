# 처음에는 무조건 주유를 해야하므로 첫 도시의 기름값 = temp
# 그 다음 도시부터 그 도시의 기름값과 temp를 비교하며 그 도시의 기름값이 더 낮다면 temp를 교체
# 이동할 때마다 temp 값과 이동거리 곱 # 수연) 오 저랑 비슷해요

import sys

n = int(input())

road = list(map(int, sys.stdin.readline().split()))

oil = list(map(int, sys.stdin.readline().split()))
# 혁) 앗! 초기값을 이렇게 줄 생각을 못했네요 좋은거 보고 갑니다
temp = oil[0]
answer = 0
for i in range(1, len(oil)):
    if oil[i] >= temp:
        answer = answer + temp * road[i-1]
    else:
        answer =answer + temp*road[i-1]
        temp = oil[i]

print(answer)
    