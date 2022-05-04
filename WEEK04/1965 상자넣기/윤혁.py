# 풀이 👉 보자마자 LIS (Longest Increasing Sequence)가 떠올라서 써버림
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

boxs = [int(x) for x in input().split()]
print(boxs)

dp = [1] * n

for i in range(n):
    for j in range(i):
        if boxs[i] > boxs[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1

# 👆 == 👇

# dp = [0] * n

# for i in range(n):
#     for j in range(i):
#         if boxs[i] > boxs[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1

print(max(dp))
