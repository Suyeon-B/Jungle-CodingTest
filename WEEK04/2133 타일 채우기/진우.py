# 참고 블로그 : https://yabmoons.tistory.com/536 그림으로 너무 잘 설명해주심
# 단순히 계산하면 중복되는 경우의 수를 거르기가 너무 힘드므로 특이한 블록을 잘 이용해야함

dp = [0 for _ in range(31)]

n = int(input())

dp[0] = 1
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i-2]             # 일반적인 경우의 수 넣고
    for j in range(4, i, 2):
        dp[i] += dp[i-j]*2              # 특이한 블록의 경우의 수 # 수연) 나는 이게 너무 어려웠어~~~~~ 다 그렸는데도
    dp[i] += 2                          # 추가되는 특이한 블록

print(dp[n])