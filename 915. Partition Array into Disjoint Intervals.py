# partition nums
# every left <= every right
# minimize len(left)
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        l_max = [None] * n
        r_min = [None] * n
        
        l_max[0]=nums[0]
        r_min[n-1]=nums[n-1]

        for i in range(1, n):
            l_max[i] = nums[i] if l_max[i-1]<nums[i] else l_max[i-1]
            r_min[n-i-1] = nums[n-i-1] if r_min[n-i]>nums[n-i-1] else r_min[n-i]
        
        for i in range(1, n):
            if l_max[i-1]<=r_min[i]:
                return i
