import sys

n,c = map(int, input().split())

house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

left = 0                                # 시작 간격
right = house[n-1]                      # 최대 간격
max_num = 0                             # 저장할 최대 거리

while left <= right:                    # 이분탐색 시작
    temp_house = house[0]               # 처음 시작하는 집의 좌표
    mid = (left + right)//2
    count = c-1                         # 첫 집에 공유기를 무조건 설치한다는 가정
    for i in house:
        if temp_house + mid <= i:       # 만약 간격내에 집이 있다면 공유기를 설치
            temp_house = i
            count = count -1
        if count == 0:                  # 모든 공유기가 설치 됐다면 반복문 종료
            max_num = max(max_num, mid)
            break
    if count == 0:                      # 모든 공유기가 설치됐다면 한번 간격을 더 올려서 확인 해본다.
        left = mid+1                    
    else:                               # 모든 공유기의 설치가 되지 않았으므로 간격을 낮춘다
        right = mid-1

print(max_num)

# 수연) 시작 간격이 저는 1이었는데 진우님은 0인 거 말고는 코드가 거의 비슷해용 ㅎㅎ 더 말씀드릴 게 없네요! 굿굿
# 그리고 공유기 설치 다 했을 때 left 값을 다시 올려 돌리는 이유가 좀 찝찝했는데 해소됐슴니당 감사해요~!