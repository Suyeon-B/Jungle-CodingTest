#bfs 문제

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip().split()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)] 

print(visited)

