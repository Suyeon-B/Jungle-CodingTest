#4 까지 그려보고, 2, 4를 활용해서 규칙성을 찾으려 했으나 실패
#참고해서 풀이완료
n = int(input())

dp = [0] * 31

dp[2] = 3

for i in range(4,n+1,2):
    dp[i] = 2+ dp[i-2]*3 + sum(dp[:i-2])*2 

    print(dp[n])