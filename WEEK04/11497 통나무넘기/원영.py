# 핵심 아이디어
# 통나무 정렬 후 작은 것 부터 왼쪽 오른쪽 번갈아서 놓았을 때 가장 난이도가 낮게 나온다.
from collections import deque
import sys
sys.stdin = open("input.txt",'r')
input = sys.stdin.readline


t= int(input())
for _ in range(t):
  n = int(input())
  log_li = [0] * n
  log = deque(sorted(list(map(int,input().split()))))

  left = 0
  right = n-1
  while left <= right:
    temp = log.popleft()
    log_li[left] = temp
    left += 1
    if len(log) == 0:
      break
    temp = log.popleft()
    log_li[right] = temp
    right -= 1
  
  answer = 0
  for i in range(n):
    if i == n-1:
      answer = max(answer, abs(log_li[i] - log_li[0]))
      break
    answer = max(answer, abs(log_li[i] - log_li[i+1]))
  print(answer)
