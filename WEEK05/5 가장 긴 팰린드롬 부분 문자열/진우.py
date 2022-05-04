# 브루트포스로 최대한 시간복잡도 줄였더니
# 아슬아슬하게 통과.. 뭔가 어거지로 푼 느낌이네요
# 혁) 풀었으면 그걸로 장땡아닐까용 ?! # 수연) 222  :: 진)파이썬 아니면 실패했을거 같아요 ㅋㅋㅋ

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start = 0
        
        answer= ''
        while True:
            end = len(s)
            if start == end:
                break
            if len(answer) > len(s[start:]):
                break
            while True:
                if start == end:
                    if len(s[start]) > len(answer):
                        answer = s[start]
                    break
                start_temp = ''
                end_temp =''
                start_temp = s[start:end]
                end_temp = start_temp[::-1]
                
                if start_temp == end_temp:
                    if len(answer) < len(start_temp):
                        answer = start_temp
                        break
                end -= 1
            start += 1
                
        return answer