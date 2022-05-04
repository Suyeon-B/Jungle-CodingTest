"""
IDEA
- 양 끝 인덱스부터 최솟값을 채워 나감
"""
from collections import deque
from sys import stdin
# stdin = open("Baekjoon/Greedy/input.txt",'r')
input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    L = list(map(int, input().strip().split()))

    L = deque(sorted(L))
    log = [0]*n
    for i in range(n//2):
        log[i] = L.popleft()
        log[n-1-i] = L.popleft()
    if n%2 == 1: # 홀수개의 통나무가 있을 때 처리
        log[n//2] = L.popleft()
    
    level = 0
    for i in range(n-1):
        level = max(level, abs(log[i]-log[i+1]))
    level = max(level, abs(log[0]-log[-1])) # 양끝 통나무 차이

    print(level)