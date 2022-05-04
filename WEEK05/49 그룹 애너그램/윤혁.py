class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 문자열 문자로 잘라
        # 정렬해 -> 같으면 같이 저장
        # 키 : [문자들] value : [원래 문자]
        dict = {}
        len_str = len(strs)
        for i in range(len_str):
            tmp = ''.join(sorted(list(strs[i])))
            if tmp in dict:
                dict[tmp].append(strs[i])
            else:
                dict[tmp] = [strs[i]]
        answer = list(dict.values())
        return answer
