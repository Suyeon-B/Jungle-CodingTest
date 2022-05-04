# 자기 제외 왼쪽 곱 * 자기 제외 오른쪽 곱 아이디어 좋네요
# 문제 잘읽고 풀겠습니다 ㅎㅎ...........
# answer 제외하고 변수 한개만 써서 O(1)로 했습니다
# 수연) 👍

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer =[]
        temp = 1
        for i in range(0,len(nums)):
            answer.append(temp)
            temp = nums[i]*temp
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i]*temp
            temp = nums[i] * temp
            
        return answer