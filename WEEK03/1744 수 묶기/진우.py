# 예외사항 처리하느라 머리 빠개지는 줄 알았네요
# 접근 방법 -> 양수의 경우 가장 큰수 * 그 다음 수
# 예외사항 : 1과 2는 곱하는거 보다 더하는게 더 높다
# 음수의 경우 가장 작은 수 * 그 다음 수
# 0 이 존재하는 경우 음수가 홀수인 경우 마지막 수랑 곱해줌

import sys

n = int(input())

nums = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    nums.append(temp)

nums.sort(reverse=True)
for i in range(len(nums)):
    if nums[i] <= 0:
        break
else: i = n
answer = 0
start = 0

# 양수
while True:
    if start == i-1:
        answer += nums[start]
        break
    if start > i-1:
        break

    if nums[start] > 2 and nums[start+1] > 1 :
        answer += nums[start] * nums[start+1]
        start +=2
    else:
        answer += nums[start]
        start +=1

start = n-1
# 음수
while True:
    if start == i:
        answer += nums[start]
        break
    if start <= i:
        break

    if nums[start] <= 0 and nums[start-1] <= 0 :
        answer += nums[start] * nums[start-1]
        start -=2
    else:
        answer += nums[start]
        start -=1

print(answer)