#손코딩 까지는 완료했는데, 잘 구현되지 않아, 소스코드 참고 # 수연) 나도~~ 
#sol.01
def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # 홀수
        tmp = self.check(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # 짝수
        tmp = self.check(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

#중앙에서 퍼져나가게 인덱스 조정해주는 함수
def check(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

#sol.02
#하나 더 생각 나는 방식이 있어서 해볼게요