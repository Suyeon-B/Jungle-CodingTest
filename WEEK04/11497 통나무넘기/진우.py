# 접근 방법 -> 차이가 최소가 되게 하기 위해 통나무를 정규분포의 형태로 만들어 주었음
# 정렬 후 가장 긴 통나무를 중심으로 균일하게 퍼지도록 만듬


import sys
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    trees = list(map(int, sys.stdin.readline().split()))

    trees.sort()

    temp = deque([])
    new_tree = deque([])
    start = len(trees)
    check = 0

    if start % 2 == 0:
        check = 1
    for i in range(start-1, -1, -1):
        if i % 2 == check:
            temp.append(trees[i])
        else:
            new_tree.appendleft(trees[i])

    while temp:
        new_tree.append(temp.popleft())

    temp = new_tree[0]
    maxs = abs(new_tree[0] - new_tree[-1])

    for i in range(1, len(new_tree)):
        if abs(temp - new_tree[i]) > maxs:
            maxs = abs(temp - new_tree[i])
        temp = new_tree[i]
    print(maxs)