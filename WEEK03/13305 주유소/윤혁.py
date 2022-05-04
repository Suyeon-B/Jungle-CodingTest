# 단순하게 최소 가격을 업데이트 해주면 되지 않을까라는 생각으로 구현
import sys

input = sys.stdin.readline

N = int(input())

roads = [int(x) for x in input().split()]

prices = [int(x) for x in input().split()]

price = 1e9
result = 0
for i in range(N-1):
    price = min(price, prices[i])
    result += price * roads[i]

print(result)

# 님 천재? 무릎 탁 치고 갑니다
# 수연) 나도 잘 생각했다고 뿌듯했는데 이게 더 쩌네 와 님 진짜 천재?
# 