class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = sum(nums)-nums[0]
        right_sum = 0
        if left_sum==right_sum: return 0
        
        for i in range(1, len(nums)):
            right_sum += nums[i-1]
            left_sum -= nums[i]
            if right_sum==left_sum:
                return i
        return -1
