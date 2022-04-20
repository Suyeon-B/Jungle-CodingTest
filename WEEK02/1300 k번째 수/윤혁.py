import sys

input = sys.stdin.readline

N = int(input())
k = int(input())


def func(x):
    count = 0
    for i in range(1, N+1):
        count += min(x//i, N)
    return count


def binary():
    left = 0
    right = k+1
    while left < right:
        mid = left + (right-left) // 2 # 수연) 이건 좀 신박하네요 책: p 524
        if func(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


print(binary())

#코드가 흥미로워용

# 수연) 함수 두 개로 깔꼼하게 짜셨군용