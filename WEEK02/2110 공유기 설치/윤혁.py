# 다시 풀기
import sys

input = sys.stdin.readline

N, C = map(int, input().split())

homes = [int(input()) for i in range(N)]

homes.sort()


def func(x):
    count = 1
    start = homes[0]
    for i in range(1, len(homes)):
        if homes[i] - start >= x:
            count += 1
            start = homes[i]
    return count


left, right = -1, 10**9+1

while left < right:
    mid = (left + right)//2
    if func(mid) >= C:
        left = mid + 1
    else:
        right = mid


print(left-1)
