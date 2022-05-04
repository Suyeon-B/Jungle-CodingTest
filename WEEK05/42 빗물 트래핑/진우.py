# 가장 긴 막대기를 mid로 정해두고
# start -> mid, mid <- end 로 풀었습니다 # 수연) 굿굿이요 나도 투 포인터 익숙해지고 싶다!!!
# 제가 화이트보드에 설명했을 때 해결하지 못한 케이스 (긴 막대 이후로 더 긴 막대가 안나오는 경우) 해결하는 가장 쉬운게 그냥 투포인터 비슷하게 푸는게 편할거 같아서 기존 코드는 왼 -> mid 였는데 여기서 오 -> mid 코드만 추가하니까 통과하네요 start, end 모두 0 높이는 스타트 지점으로 안잡았어요~ # 수연) LGTM!
# LGTM!


class Solution:
    def trap(self, height: List[int]) -> int:
        mid = [0, 0]
        start = [0, 0]
        end = [0, 0]
        for i in range(len(height)):
            if start[0] == 0 and height[i] != 0:
                start = [height[i], i]
            if mid[0] < height[i]:
                mid = [height[i], i]

        for i in range(len(height) - 1, -1, -1):
            if height[i] != 0:
                end = [height[i], i]
                break
        result = 0

        # 시작부터 미드

        for i in range(start[1] + 1, mid[1] + 1):
            if start[0] <= height[i]:
                result += (i - start[1] - 1) * start[0]
                for j in range(start[1] + 1, i):
                    result -= height[j]
                start = [height[i], i]

        # 끝부터 미드
        for i in range(end[1] - 1, mid[1] - 1, -1):
            if end[0] <= height[i]:
                result += (end[1] - i - 1) * end[0]
                for j in range(end[1] - 1, i, -1):
                    result -= height[j]
                end = [height[i], i]
        return result
