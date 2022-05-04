# 투포인터는 사랑입니다

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        i = 0
        answer = set()
        while i <= len(nums)-2:
            start = i+1
            end = len(nums)-1
            while start != end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start +=1
                else:
                    answer.add((nums[i],nums[start],nums[end]))
                    start +=1
            i +=1
        
        
        return answer