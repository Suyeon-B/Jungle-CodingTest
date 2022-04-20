#bfs 문제


# 섬 영역별로 좌표 구하기
# 다리 제작
# 최소 스패닝 트리 수행

# 주의사항
# 1. 다리에 육지가 있어서는 안됨
# 2. 다리의 길이가 2보다 짧으면 안됨
# 3. 다리는 직선이어야함
# 4. 다리의 양 끝점에 육지가 존재해야함
# * 섬의 위치가 적절하지 않은때, 다리 개수가 부족할 때 print(-1)


# 구현
# 최소 스패닝 트리 - 크루스칼

from collections import deque
import sys, heapq

sys.stdin = open("input.txt")
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 섬 구분하여 좌표 구하기 (BFS)

#다리 제작

#크루스칼 

