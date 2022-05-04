from collections import deque

height = [4,2,0,3,2,5]

#최대 높이 만큼 돌면서
#양끝이 양수면 카운트 시작 -> 투 포인터를 활용하면 될꺼같은데 무리
#카운트: 0 보다 작은수 세기
#예제의 경우 마지막줄에 양수가 하나이기 때문에 그룹핑을 할 수 가 없다 ∴ 0

a = len(height)

height = deque(height)
count = 0 

for _ in range(1, max(height)+1): # 첫줄에서는 문제 없이 동작 
    for _ in range(len(height)):
        if height[0] <= 0:
            height.popleft()
            # j += 1
            

        if height[len(height)-1] <= 0:
            height.pop()
            # a -= 1
        #두번째 여기서 부터 바로 카운트로 넘어가네
    for i in height:
        if i <= 0:
            count+= 1
    for i in range(len(height)):
        height[i] -= 1
    print(height)

  