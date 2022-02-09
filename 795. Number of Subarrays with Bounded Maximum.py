class Solution:
    # 满足条件的subarray：最大值在[left, right]之间
    # o [left, right]: 单独满足
    # . <left: 和附近的o组合满足
    # x >right: 不满足
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # 找到所有不满足的，用不满足的把nums分成多个array
        # 对每个array: 所有组合数 - 只包含.的组合数
        # 长度为n的array中的subarray数：(n+1)*n/2
        res = 0
        i, j = 0,0
        while i<len(nums) and j<len(nums):
            while i<len(nums) and nums[i]>right:
                i+=1
            if i>=len(nums):
                return res
            j=i+1
            while j<len(nums) and nums[j]<=right:
                j+=1
            # found subarray with "o", "."
            cur = nums[i:j]
            res += self.find(cur, left, right)
            # next
            i=j+1
        return res

    def find(self, cur, left, right):
        res = (len(cur)+1)*len(cur)//2
        i,j = 0,0
        while i<len(cur) and j<len(cur):
            while i<len(cur) and cur[i]>=left:
                i+=1
            if i==len(cur):
                return res
            j=i+1
            while j<len(cur) and cur[j]<left:
                j+=1
            # found subarray with "."
            res -= (j-i+1)*(j-i)//2
            i=j+1
        return res
                