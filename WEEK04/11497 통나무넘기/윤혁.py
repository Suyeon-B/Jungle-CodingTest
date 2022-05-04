import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    logs = [int(x) for x in input().split()]
    logs.sort()
    answer = 0
    # 처음에는 오름차순 내림차순 정렬을 두번해서 하려했는데
    # 하다보니 아래 방법이 더효율적일것 같아 아래방법을 사용
    # [i]랑 [i-1]차이보다 [i] [i-2]차이가 더 크니 얘네만 비교
    for i in range(2, N):
        answer = max(answer, abs(logs[i] - logs[i-2]))
    print(answer)

# 이분 코드 수 줄여서 쓰는거 장인이네 # 수연) 222
# ... 진짜 다 이렇게 풀 줄