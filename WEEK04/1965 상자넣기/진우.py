# LIS 날먹

import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))