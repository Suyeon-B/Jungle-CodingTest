## 오늘 풀이
import sys
from collections import defaultdict

input = sys.stdin.readline

arr = input().strip()

dic = defaultdict(int)

for w in arr:
  dic[w] +=1

temp = 0
for i in dic:
  if dic[i] %2 !=0:
    temp +=1
if temp >1:
  print("I'm Sorry Hansoo")
  exit(0)

dic = dict(sorted(dic.items()))

s = ""
temp = ''
for key in dic:
  while dic[key] >1:
    s += key
    dic[key] -= 2
  if dic[key] == 1:
    temp = key

print(s+temp+s[::-1])

# 예전 풀이
names = input()
name_cnt = [0 for _ in range(26)]
for name in names:
    name_cnt[ord(name)-65] += 1
    
odd = 0
odd_alpha = ''
alpha = ''
for i in range(26):
    if name_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i+65)
    alpha += chr(i+65) * (name_cnt[i] // 2)
        
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1])