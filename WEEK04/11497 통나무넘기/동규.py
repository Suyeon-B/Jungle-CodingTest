#정렬을 통해 가운대 최대값을 넣고 그나음부터 왼-오-왼-오 큰수들을 차례대로 채워감
#그리고 최종적으로 차(절댓값)들의 리스트를 구한다음, 제일 큰 값을 출력
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    # print(nums)
    tmp = [0] * n
    ans = []
    #최대값 넣을 인덱스 구해서 넣기
    tmp[(n // 2)] = nums[0]
    count = 1 #num의 인덱스

    for i in range(1, (n//2)+1):
        tmp[(n//2) - i] = nums[count]
        count += 1 

        if count < len(tmp):
            tmp[(n//2) + i] = nums[count] 
            count += 1
#리스트 완료
    #절댓값 차들을 리스트에 저장
    for i in range(1, len(tmp)):
        ans.append(abs(tmp[i-1]-tmp[i]))
    print(max(ans))