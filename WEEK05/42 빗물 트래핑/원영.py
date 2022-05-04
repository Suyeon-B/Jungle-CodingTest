# 이해가 안되서 다시보고 정리하겠습니다.
class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        current = 0
        answer = 0
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] -1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                answer += distance * bounded_height

            stack.append(current)
            current+=1x

        return(answer)
