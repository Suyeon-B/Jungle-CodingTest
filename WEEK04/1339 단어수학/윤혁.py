# https://www.acmicpc.net/problem/1339
# IDEA
# 가장 긴놈(idx제일 큰놈) 찾아서 앞에서부터 가장 자주 나오는 애 9 주기
# 76543210 idx안에 [0 *26] 알파벳 찾아서
# 해당 인덱스에 가장 많이 등장하는 친구를 찾아서 9,8,7 ... 주려고했음
# 시간 복잡도가 n^3이 나와서 도중에 포기
# 밑은 정답 풀이임 다음에 풀어보기 위해 제출하지 않아 메모리, 시간은 알 수 없음
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

word = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)]

alpha = [0] * 26

for i in range(n):
    j = 0
    for w in word[i][::-1]:
        alpha[w] += (10**j)
        j += 1

alpha.sort(reverse=True)
ans, t = 0, 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (t*alpha[i])
    t -= 1
print(ans)

