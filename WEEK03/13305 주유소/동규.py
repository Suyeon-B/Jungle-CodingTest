import sys

# sys.stdin = open("input.txt")


n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum = 0
mini = cost[0]

for i in range(1, n+1):
    if cost[0] < mini:
        mini = cost[i]
    sum += mini * road[i]

print(sum)

#참조해서 완성했숩니다
