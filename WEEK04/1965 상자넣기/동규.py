 # 브루트 포스로 가능할 것같지만 이전 dp문제들 처럼 생각해보면 정말간단한 점화식이 하나 나올꺼 같은 느낌
# 오른쪽에서 부터 하나 씩 줄여가며 최대로 몇개가 가능한지 체크 -> 역순으로 해서 왼쪽부터(?)
# 엑셀에 있는 LIS 문제 풀고 바로함

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp  = [1] * (N)
print(nums)
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))