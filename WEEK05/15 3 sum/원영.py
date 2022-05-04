# 항상 투포인트는 대단하다고 느낌 ㅎㅎ
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answer = []
        result = set()
        for i in range(len(nums)):
          temp = nums[i]
          left = i+1
          right = len(nums)-1
          while left < right:
            sum_3 = temp + nums[left] + nums[right]
            if sum_3 > 0:
              right -=1
            elif sum_3 < 0:
              left +=1
            else:
              result.add((temp, nums[left], nums[right]))
              left +=1
              right -=1
        for i in result:
          answer.append(i)
        return(answer)