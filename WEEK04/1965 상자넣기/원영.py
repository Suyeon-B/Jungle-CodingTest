# 가장 긴 증가하는 수열(LIS)과 같은 알고리즘이다.
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int ,input().split()))

answer = [1]*n

for i in range(n):
  for j in range(i):
    if nums[i] > nums[j]:
      answer[i] = max(answer[i], answer[j]+1)

print(max(answer))