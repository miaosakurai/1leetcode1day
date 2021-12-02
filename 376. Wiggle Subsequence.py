class Solution:
    # find wiggle sequence转化为找单调性变化的次数
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        res = 1
        inc = True
        start = 0
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                if nums[i]<nums[i-1]:
                    inc = False
                else:
                    inc = True
                res +=1
                start = i
                break
        
        for i in range(start+1, len(nums)):
            if (nums[i]<nums[i-1] and inc) or (nums[i]>nums[i-1] and not inc):
                res +=1
                inc = not inc
        return res
            