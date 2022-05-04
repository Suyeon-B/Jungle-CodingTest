from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = deepcopy(strs)
        dic = defaultdict(list)
        for idx, val in enumerate(temp):
          t = sorted(list(val))
          dic[''.join(t)].append(idx)
        answer = []
        for key in dic:
          t = []
          for i in dic[key]:
            t.append(strs[i])
          answer.append(t)

        return answer