# 사전순 출력 안해서 틀렸었네유
# set으로 중복 제거, 홀수 찾고 홀수 두개 이상이면 false
# front, mid, end 세개로 나눠서 저장후 합쳤습니다

import sys
from collections import deque

name = sys.stdin.readline().rstrip()

name = list(name)
name.sort()
check = set(name)
name = deque(name)

front = []
end = deque()

count_s = 0
count_list = []
mid = []
for i in check:
    if name.count(i) % 2 != 0:
        count_s +=1
        count_list.append(i)

if count_s > 1:
    print("I'm Sorry Hansoo")
else:
    while name:
        if len(count_list) > 0:
            if count_list[0] == name[0]:
                count_list.pop()
                mid.append(name.popleft())
                continue
        front.append(name.popleft())
        if len(name) == 0:
            break
        end.appendleft(name.popleft())

end = list(end)

answer = front +mid + end
answer = ''.join(answer)
temp = answer[::-1]
if answer == temp:
    print(answer)
else:
    print("I'm Sorry Hansoo")