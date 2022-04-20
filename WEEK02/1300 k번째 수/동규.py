#sol.1 - 당연히 실패 
import sys

input = sys.stdin.readline

A = []
B = []

N = int(input())
K = int(input())
for i in range(1, N+1):
    for j in range(1, N+1):
        B.append(i * j)

B.sort()
print(B[K])

# 시간 초과가 나나용?

#sol.2 #규칙성을 찾으려고 노력해보기!(알고보니 너무 간단했다..) # 수연) 님 재천? 나는 봐도 안 간단하던데...
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start = 0
end = k
#tmp, count -> 문제에서 활용하는 법 숙달하기 // 언제 어떻게 무엇을 왜?

import sys

n = int(input())
k = int(input())

start = 0
end = k
answer = 0
while start <= end:
    mid = (start + end ) // 2
    count = 0

    for i in range(1, n+1):
        count += min(mid//i, n)

    if count >= k:
        answer = mid
        end = mid - 1
        
    else:
        start = mid + 1

print(answer)

# 수연) 여러분 answer = mid 이렇게 푸는 거 토론 좀 해봤으면 좋겠슈 
# + 그리고 start <= end 와 start < end의 차이에 대해서도 ...

"""
수연) 제가 혼자 생각해본.. 틀린 생각이면 고쳐줘야 하는 이야기 ⬇️⬇️⬇️
answer = mid로 따로 저장한 뒤 출력하지 않아도
start나 end로 답을 출력하는 방법은,

k와 같아지는 순간에 end던 start던 마지막으로 +1 / -1 한 뒤 한 번 더 체크하는데,
이 때 값의 변화가 마지막에 없는 애(만약 end = mid-1 로 while문을 마지막으로 돌았다면 start가 마지막 변화 없는 애)가 답이 된다고 생각합니다@!0

왜냐면 예를 들어서 지금 동규오빠 코드에서는 count == k일 때 
start와 end가 겹쳐질랑말랑 하는 찰나의 순간에~? 
count == k가 되고 end=mid-1로 바꿔서 확인 한 번 한 뒤 끝나잖아요?

그러니까 count == k 일 때 건드린 end 말고 start가 답이다~ 하는 말이에용

여러분의 생각은? 🎤
"""