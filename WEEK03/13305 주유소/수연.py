"""
100점~!
두 개의 변수 사용
min_sofar -> 현재까지의 최솟값
MIN -> 전체 배열의 최솟값

지금 들르는 주유소가 min_sofar보다 비싸면 min_sofar금액으로 주유하고, 
min_sofar보다 저렴하면 min_sofar을 바꿔주고 주유함

중간에 MIN값을 만나면 뒷쪽은 바로 더해서 break
"""
import sys
sys.stdin = open("Baekjoon/Greedy/input.txt",'r')
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().strip().split()))
juyouso = list(map(int, input().strip().split()))

min_sofar = juyouso[0]
MIN = min(juyouso[:-1])
result = 0
for i in range(n):
    if juyouso[i] == MIN:
        result += MIN*sum(cost[i:])
        break
    elif juyouso[i] >= min_sofar:
        result += min_sofar*cost[i]
    elif juyouso[i] < min_sofar:
        min_sofar = juyouso[i]
        result += min_sofar*cost[i]

print(result)