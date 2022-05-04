"""
그려서 특수한 경우를 세어보다가 규칙을 모르겠어서 답봤음
멀고도 험한 점화식의 길 ...
"""
from sys import stdin
# stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

n = int(input().strip())
tiles = [1]*31
tiles[2] = 3
if n%2 == 1:
    print(0)
    exit(0)

for i in range(4, n+1):
    tiles[i] = tiles[2] * tiles[i-2]
    for j in range(i-4, -1, -2):
        tiles[i] += tiles[j] * 2

print(tiles[n])
