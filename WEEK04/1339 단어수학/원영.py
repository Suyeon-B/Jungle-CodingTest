import sys
from collections import defaultdict

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
dict = defaultdict(int)
# 각 단어의 자리 수 값을 딕셔너리에 저장한다
# A자리가 10의 자리면 {'A':10} 의 형태로 저장됨
for _ in range(N):
  input_alpha = list(input().strip())
  input_alpha.reverse() # 수연) 와 이거 좀 천재
  
  for i in range(len(input_alpha)-1, -1, -1):
    dict[input_alpha[i]] += 10 ** i

# 딕셔너리 value값으로 내림차순 정렬
dict = sorted(dict.items(), key= lambda x:x[1], reverse=True)
answer = 0
idx = 9
# value가 높은 값부터 차례대로 숫자 넣고 계산
for i in dict:
  answer += i[1]*idx
  idx-=1
print(answer)

# 짱깔끔하게 잘풀었네
# 수연) 질문! 빈도수 계산은 언제 하나여?
  # 자리수 계산할 때 다 더해짐 ABA 이면 A 는 101이 됨. 
  # 그래서 많이 나오면 순위가 높아짐
