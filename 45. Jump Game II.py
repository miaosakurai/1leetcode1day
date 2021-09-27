class Solution:
    def jump(self, nums: List[int]) -> int:
        # for i range from right to left: find leftmost index that can jump to i
        i = len(nums)-1
        step = 0
        while i>0:
            for j in range(i):
                if nums[j]>=i-j:
                    i=j
                    step+=1
                    break
        return step