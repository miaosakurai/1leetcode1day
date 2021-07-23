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

    def partitionDisjoint2(self, nums: List[int]) -> int:
        l_maxs = [0] * len(nums) 
        r_mins = [0] * len(nums)
        
        l_maxs[0] = nums[0]
        r_mins[-1] = nums[-1]
        
        for i in reversed(range(len(nums)-1)):
            r_mins[i] = min(r_mins[i+1], nums[i])
        
        for i in range(len(nums)-1):
            l_maxs[i] = max(l_maxs[i-1], nums[i])
            if l_maxs[i]<=r_mins[i+1]:
                return i+1
        