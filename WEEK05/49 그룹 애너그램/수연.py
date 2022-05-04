"""
IDEA
- 모든 문자를 set으로 받아 정렬한 값을 value로 딕셔너리에 넣고,
- value값이 일치하면 한 묶음으로 넣음

대충격
정답코드는 4줄이네여..... ㅎㅎ
정렬된 값을 Key로 value에 str들을 넣어준 뒤 list 형으로 출력해주면 끝임!!!
"""
#고생했어.... 와우

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 들어온 문자열이 없을 때 예외처리
        if len(strs) == 1:
            return strs
            exit(0)

        # 우선 모든 문자를 set으로 받아 정렬한 값을 value로 딕셔너리에 넣는다.
        sorted_strs=[]
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))

        dict = {}
        for i in range(len(strs)):
            dict[strs[i]] = "".join(sorted(strs[i]))


        # value값이 일치하면 한 묶음으로 넣는다.
        answers = [[] for i in range(len(set(sorted_strs)))]
        now = 0
        check = [False]*len(strs)
        answers[0].append(strs[now])
        check[0] = True
        idx = 0

        next = 1
        while True:
            for i in range(next, len(strs)):
                if dict[strs[now]] == dict[strs[i]] and not check[i]:
                    answers[idx].append(strs[i])
                    check[i] = True
                else:
                    if next == now+1 and not check[i]:
                        next = i
            if next == len(strs)-1:
                for answer in answers:
                    if answer:
                        if dict[answer[0]] == dict[strs[-1]]:
                            answer.append(str[-1])
                            check[-1] = True
                    else:
                        answer.append(strs[-1])
                        check[-1] = True
            if len(set(check))==1:
                return answers
                exit(0)
            idx += 1
            now = next
            answers[idx].append(strs[now])
            check[next] = True
            next = now+1


# 아래는 정답코드
"""
from collections import defaultdict
# strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = defaultdict(list)
        
for word in strs:
    anagrams[''.join(sorted(word))].append(word)
print(list(anagrams.values()))
"""