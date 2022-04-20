# 2110 
"""
두 집 사이의 거리(gap)를 가지고 이분탐색
적절한 gap일 때 '공유기 설치 cnt 값 == 주어진 공유기의 개수' 조건이 맞게 됨.
"""

import sys

n, c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 1, houses[-1]-houses[0] # 간격의 최소, 최대값
while s<=e:
    gap = (s+e)//2 # 두 집 사이의 거리
    cnt = 1
    now = houses[0]

    for house in houses:
        if now+gap <= house: # gap 만큼 벌어진 다음 집에 공유기 설치
            cnt+=1
            now = house
    
    if cnt >= c: # 주어진 공유기 개수보다 많이 셌으면 더 간격 넓혀도 됨
        s = gap+1
        answer = gap # ❓❓❓ 여기 궁금함. 이 때의 gap을 반복문 끝나고서 그냥 print하면 틀림
      # 문제의 예제에 거리 2를 대입하면 cnt가 3이되고 이 조건에 만족하게 됩니다.
      # 이때 반복문을 끝내면 답이 2가 되어 오답이 나오게 됩니다.
      # 😳 오 대박 님 재천?
    else: # 간격 좁히기
        e = gap-1

print(answer)

"""
⬇️⬇️⬇️ retry 버전 ⬇️⬇️⬇️

import sys

n,c = map(int, sys.stdin.readline().strip().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

s, e = 1, houses[-1]-houses[0] # 간격의 최소, 최대값
while s<=e:
    gap = (s+e)//2 # 두 집 사이의 거리
    now = houses[0] # 현재 공유기를 설치한 집
    cnt = 1 # 공유기 개수

    for i in range(1, n):
        if now+gap <= houses[i]:
            cnt += 1
            now = houses[i]
    
    if cnt >= c: # 공유기 너무 많이 설치. gap 넓혀야 함
        s = gap+1
    else: # 공유기 적게 설치. gap 줄여야 함
        e = gap-1

print(e) # 처음 버전 답과 다른 점 : e를 애초에 간격의 최대값으로 설정했으므로, 
                               반복문이 끝난 뒤의 e가 정답임

"""


