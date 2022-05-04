# dp[2] = 3
# dp[4] = dp[4-2]*3 + dp[4-4]*2 +2
# dp[6] = dp[6-2]*3 + dp[6-4]*2 + dp[6-6]*2 +2
# 요로코롬 점화식 구하는 예시 보고 코드 
import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline

n = int(input())
dp = [0] * (31)
dp[2] = 3
for i in range(4, 31):
  if i %2 == 0:
    dp[i] += dp[i-2]*3 +2
    for j in range(0,i-2, 2):
      dp[i] += dp[j]*2

print(dp[n])