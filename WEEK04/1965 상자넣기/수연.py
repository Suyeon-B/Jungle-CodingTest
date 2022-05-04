# 이분탐색 풀이 ver.
# LIS 문제와 동일
# ???????? 상자넣기아님? 아하하하 맞네요 쏘리
# goood
# 이건 상자넣기 아닌가여????
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

def find_idx(list, k):
    l, r = 0, len(list)-1
    while l<r:
        m = l+(r-l)//2
        if list[m] < k:
            l = m+1
        else:
            r = m
    return l

def LIS():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    cnt = 0

    lis = [A[0]] + [1e9]*(n-1)

    for i in range(1, n):
        idx = find_idx(lis, A[i])
        lis[idx] = A[i]
    
    for i in range(n):
        if lis[i] != 1e9:
            cnt+=1
    
    print(cnt)

LIS()

# DP로 풀어본 LIS
# 기준 값을 변경하며 최소한만 확인한다.
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

def LIS():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))

    dp = [1] * (n+1)
    for i in range(1, n):
        for j in range(0, i): 
            if A[i] > A[j]: # A[i] > A[j] 일 때 앞쪽만 확인해서 LIS를 갱신한다.
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))

LIS()