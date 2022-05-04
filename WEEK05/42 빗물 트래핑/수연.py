# TLE 코드
# 화이트 보드에 설명했던, 끝 벽이 0일 때의 bug는 잡았지만..
# 근본적으로 O(n^2) 풀이로는 시간 초과여서 투 포인터로 다시 풀어봤습니당.
# 시간초과 걸린 Test Case 보니까 n백줄짜리 리스트로 들어오더라고요 ^^..
def main():
    height = [5, 4, 1, 2]
    size = len(height)
    rain = [0] * size
    result = 0
    trigger = False
    while sum(height) > 1:
        for i in range(size):
            if height[i] > 0:
                rain[i] = 1
                height[i] -= 1
        for j in range(size-1):
            if rain[j] > 0 and not trigger:
                trigger = True
            if rain[j] == 0 and trigger and sum(rain[j:]) > 0:
                result += 1
        rain = [0] * size
        trigger = False
    return result


print(main())


# 투 포인터를 활용한 풀이 retry
# 지금까지의 최대 높이와 현재 높이를 빼서 더해나간다.
# ㄴ> 지금까지의 최대 높이는 투 포인터의 idx를 조정해서 갱신한다.

def main():
    height = [4, 2, 0, 3, 2, 1]

    if not height:
        return 0

    volume = 0
    left, right = 0, len(height)-1  # 투 포인터의 idx
    left_max, right_max = height[left], height[right]

    # 투 포인터를 양 끝부터 시작해서
    # left와 right가 맞닿을 때 까지의 빗물 양을 cnt
    while left < right:
        # 포인터가 이동했을 때의 벽 높이와, 현재까지의 벽 높이 중 큰 값으로 max값을 조정한다.
        left_max, right_max = max(left_max, height[left]), max(
            right_max, height[right])

        # 만약 왼쪽 max값이 오른쪽 max값보다 작거나 같다면,
        # 오른쪽으로 한 칸 포인터를 이동한다.
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(main())
