"""
IDEA
- try 1: prefix, suffix 배열에 저장 후, 차례로 곱함
  -> space complexity O(n)
- try 2: prefix, suffix값을 바로 output 배열에 반영
  -> space complexity O(1)

🔊 화이트 보드에서 발표한 풀이에서 O(1)로 수정해봤습니당
"""
# 진우) 아이디어 인정.. # 수연) 감삼다 ^__^
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        output = []

        # get prefix
        for i in range(n):
            output.append(prefix)
            prefix *= nums[i]
          
        # get suffix
        prefix = 1
        for i in range(n-1, -1, -1):
            output[i] *= prefix
            prefix *= nums[i]

        return output


"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = collections.deque([1])
        suffix = [1]

        # get prefix
        for i in range(1, len(nums)):
            result = prefix[-i]*nums[-i]
            prefix.appendleft(result)
        # get suffix
        for i in range(1, len(nums)):
            result = suffix[i-1]*nums[i-1]
            suffix.append(result)

        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])

        return result
"""