#sol.1
from collections import defaultdict

ans = defaultdict(list) # 아이디어 참고 (애용하겠습니다!)


for i in strs:
    ans[''.join(sorted(i))].append(i)
    

print(list(ans.values()))

#sol.2
from collections import defaultdict

anagrams = defaultdict(list)
for string in strs:
    anagrams[tuple(sorted(string))].append(string) 
print(anagrams)
