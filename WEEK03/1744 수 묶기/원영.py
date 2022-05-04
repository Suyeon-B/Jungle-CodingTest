import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = int(input())
posi = []
nega = []
answer = 0
for _ in range(n):
  num = int(input())
  if num >1:
    posi.append(num)
  elif num == 1:
    answer +=1
  else:
    nega.append(num)

posi.sort(reverse = True)
nega.sort()

idx = 0
while idx < len(posi):
  if idx == len(posi)-1:
    answer += posi[idx]
    break
  answer += posi[idx] * posi[idx+1]
  idx+=2

idx = 0

if len(nega) % 2 == 0:
  for i in range(0, len(nega), 2):
    answer += nega[i] * nega[i+1]
else:
  for i in range(0, len(nega)-1, 2):
    answer += nega[i] * nega[i+1]
  answer += nega[len(nega)-1]

print(answer)



# # 마이너스는 거꾸로 곱해줘야 할거 같음
# import sys
# sys.stdin = open("input_py.txt", "r")
# input = sys.stdin.readline

# n = int(input())
# numbers = []
# for _ in range(n):
#   numbers.append(int(input()))
# numbers = sorted(numbers, reverse=True)

# minus = 0
# temp = 0
# for i in range(n):
#   if numbers[i] >=0:
#     temp = i
#   else:
#     minus +=1

# answer = 0

# if n == 1:
#   print(numbers[0])
#   exit(0)

# idx = 0
# while idx < temp:
#   if idx == temp and minus ==0:
#     answer += numbers[idx]
#     idx+=1
#     break
#   if idx == temp+1:
    
#     break

#   if numbers[idx] > 1 and numbers[idx+1] >1:
#     answer += numbers[idx] * numbers[idx+1]
#     idx +=2
#     continue
  
#   if numbers[idx] == 1:
#     answer+= numbers[idx]
#     idx+=1
#     continue

#   answer += numbers[idx]
#   idx+=1

# # idx = temp
# while True:
#   if idx == n-1:
#     answer += numbers[idx]
#     break
#   if idx == n:
    
#     break
#   if numbers[idx] == 0 and numbers[idx+1] < 0 and minus %2 != 0:
#     idx+=2
#     continue
  
#   if numbers[idx] <0 and numbers[idx+1] <0 :
#     answer += numbers[idx]* numbers[idx+1]
#     idx +=2
#     continue
#   if numbers[idx] == 1:
#     answer+= numbers[idx]
#     idx+=1
#     continue
#   answer += numbers[idx]
#   idx+=1

# print(answer)