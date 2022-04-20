# 모든 배열을 선언하면 메모리가 40GB가 필요하기 때문에 공간 복잡도를 줄이기 위한 방법을 생각해봐야한다.
# 수연) 메모리가 40GB일 것을 어떻게 미리 계산하시는건지 꿀팁좀여?
# 배열에 들어가는 int 하나당 4byte로 두고 계산하면 됩니다~!

n = int(input())
k = int(input())

left = 1                                # 1*1 부터 시작이므로 가장 작은 값은 1
right = k                               # k번째 수는 k 값보다 클 수가 없다
answer = 0
while left <= right:
    mid = (left + right)//2
    temp = 0
    for i in range(1,n+1):
        temp = temp + min(mid//i, n)        # 만약 n은 3인데 mid가 5라면 1행일 때 5가 되는데, 그건 불가능 최대값은 n이다.
                                            # 논리 구조 : mid / n 행 = 그 행에서 mid 이하의 숫자 개수    
    if temp >= k:
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)

# 저랑 똑같이 짜셧는데 왜 저보다 느린거죠 ?! <- 그러게요..? <- 수연) 저가 누구시죠?

# 주석보고 몰랐던 부분을 이해했습니다 ㅎㅎ