# 정답 코드
# python에 maxsize는 처음 사용해보네용!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        now = sys.maxsize
        for price in prices: # list size 구하는 것 보다 이 방법이 더 pythonic 한 것 같아서 좋은 것 같아요
            now = min(price, now)
            profit = max(price - now, profit)

        return profit

"""
try 2) 다시 풀어본 코드

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        now = prices[0]
        result = 0
        for i in range(1, n):
            now = min(prices[i], now)
            result = max(prices[i] - now, result)

        return result
"""
"""
try 1) TLE 코드

def main():
    prices = [7, 1, 5, 3, 6, 4]

    n = len(prices)
    result = 0
    for i in range(n-1):
        now = prices[i]
        later = max(prices[i+1:])
        result = max(later - now, result)

    return result


print(main())
"""