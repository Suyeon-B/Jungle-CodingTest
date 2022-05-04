"""
화이트 보드에서 말한 그대로, 한 값을 고정해서 나머지 값들 중 투 포인터를 돌렸슴당

궁금한 점
1. 왜 주석처리한 부분을 추가하면 Runtime Error일까요~?
2. 정답 코드에서 i index일 때 투 포인터가 i 자신을 가리킬 경우 어떻게 처리되나요? 
  이 경우에 문제 조건에 위배되지 않나용?
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) < 3:
        #     return nums

        left, right = 0, len(nums)-2
        triplets_sum = 0
        triplets = []
        arr = result = []
        nums = sorted(nums, reverse=True)

        for i in range(len(nums)):
            curr = nums[i]
            arr = nums[:i]+nums[i+1:]
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                triplets_sum = arr[left] + arr[right]
                if triplets_sum + curr == 0:
                    result = sorted([curr, arr[left], arr[right]])
                    triplets.append(tuple(result))
                    left += 1
                    right -= 1
                elif triplets_sum + curr > 0:  # sum값을 줄여야 할 때
                    left += 1
                else:
                    right -= 1
            left, right = 0, len(nums)-2

        triplets = list(set(triplets))
        triplets = [list(triplet) for triplet in triplets]
        return triplets