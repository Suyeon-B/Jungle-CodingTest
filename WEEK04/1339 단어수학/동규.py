# #문제조건에 대문자로 이루어져있다 -> 아스키? -> 풀다보니깐 아닌거 같은데... -> 만약에 별도의 조건이 없었을 때 대소문자가 섞여 있어도 그냥 lower 나 upper로 통일 하면 됐음
#조건이 두개가 있어야겠다(우선순위순)
#1. 자리수가 높은 쪽일 수록 9를 배치
#단) 절대적이지 않을 수가 있음, 중복 알파벳에 따라 차이가 있을 수가 있음
#예제3번과 같은 경우 9부터 차례대로 ...
#역순을 구해서 자리수 맞추는것 까지 생각함

import sys

input = sys.stdin.readline

n = int(input())

words = []
for i in range(n):
    words.append(input().strip())

dic = {}

for word in words:
    root = len(word) - 1
    for j in word:
        if j in dic:
            dic[j] += pow(10, root)
        else:
            dic[j] = pow(10, root)
        root -= 1

dic = sorted(dic.values(), reverse=True)

result, m = 0, 9

for value in dic:
    result += value * m
    m -= 1
print(result)