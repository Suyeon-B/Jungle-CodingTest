# 첫 접근 방식 -> dict 초기화 후 가장 높은 자릿수의 알파벳을 9부터 시작해서 주었음 하지만 틀림
# 예외 사항 -> ABB, BB, BB ,BB ,BB ,BB , BB, BB ,BB BB
# 예외사항 처리하는 걸 코드로 구현하지 못하겠어서 결국 답 참조
# 10의 제곱수를 이용해 자릿수로 계산하는 방법은 생각을 못했었다. 복습하고 나중에 비슷한 문제에 써먹어봐야 할듯

import sys
from string import ascii_uppercase # 수연) 오 이거 저도 써보겠습니다.

n = int(input())

dict = {}

for i in ascii_uppercase:
    dict[i] = 0

strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().rstrip())


for string in strings:
    for i in range(len(string)):
        dict[string[i]] += 10**(len(string)-i-1)

result = []

for value in dict.values():
    result.append(value)

result.sort(reverse=True)
start = 9
answer = 0

for i in result:
    answer += i*start
    start-=1
    if start == -1:
        break

print(answer)