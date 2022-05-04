'''
투포인트로 해보려고 했으나 양옆에서 조사하는 걸로 접근하여 망했습니다.
풀이 시간이 길어져서 정답 봤어요
max에도 key값 설명이 가능하단것을 처음 알게 되었네요 # 수연) 222
'''
def longest_palindrome():
    s = "babadasdfasdf"

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    if len(s) < 2 or s == s[::-1]:
        return s
    result = ""
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result

print(longest_palindrome())

# 틀린코드 ㅎㅎ 투포인트를 이상하게 씀
# def check(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# def longestPalindrome(s: str) -> str:
#     if len(s) == 1:
#         return s
#     left = 0
#     right = len(s)-1

#     while left < right:
#         if s[left] == s[right]:
#             if check(s[left:right+1]):
#                 return s[left:right+1]
#         else:
#             if s[left] == s[right-1]:
#                 right-=1
#                 continue
#             elif s[left+1] == s[right]:
#                 left +=1
#                 continue
#             right-=1
#             left+=1
    
#     return s[left: right+1]

# ss = longestPalindrome("eabcb")
# print(ss)