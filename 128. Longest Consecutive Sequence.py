class Solution:
    # sort1
    def longestConsecutive(self, nums) -> int:
        nums = sorted(nums)
        lcs = 0
        i = 0
        while i<len(nums):
            cur = 1
            j = i+1
            while j<len(nums):
                if nums[j]==nums[j-1]+1:
                    cur+=1
                    j+=1
                elif nums[j]==nums[j-1]:
                    j+=1
                else:
                    break
            lcs = max(cur, lcs)
            i = j
        return lcs

    # sort2
    def longestConsecutive2(self, nums) -> int:
        if len(nums)==0: return 0
        nums = sorted(nums)
        lcs = 0
        cur = 1
        for i in range(1, len(nums)):
            print(cur)
            if nums[i]!=nums[i-1]:
                if nums[i]-nums[i-1]==1:
                    cur+=1
                else:
                    lcs = max(lcs, cur)
                    cur = 1
        lcs = max(lcs, cur)
        return lcs

    # O(n), 参考discussion
    def longestConsecutive3(self, nums) -> int:
        nums = set(nums)
        lcs = 0
        for x in nums:
            if x-1 not in nums:  # a start point
                y = x+1
                while y in nums:
                    y+=1
                lcs = max(lcs, y-x)
        return lcs
    