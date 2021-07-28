# 3Sum Closest    
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i]+nums[j]+nums[j+1]>=target:
                    if abs(nums[i]+nums[j]+nums[j+1]-target)<abs(res-target):
                        res = nums[i]+nums[j]+nums[j+1]
                    continue
                if nums[i]+nums[j]+nums[-1]<=target:
                    if abs(nums[i]+nums[j]+nums[-1]-target)<abs(res-target):
                        res = nums[i]+nums[j]+nums[-1]
                    continue
                for k in range(j+1, len(nums)):
                    if abs(nums[i]+nums[j]+nums[k]-target)<abs(res-target):
                        res = nums[i]+nums[j]+nums[k]
        return res

    # two pointers
    def threeSumClosest2(self, nums, target) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while (r>l):
                if abs(nums[i]+nums[l]+nums[r]-target)<abs(res-target):
                    res = nums[i]+nums[l]+nums[r]
                if nums[i]+nums[l]+nums[r]>target:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<target:
                    l+=1
                else:
                    return target
        return res