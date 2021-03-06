class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r,r2l,res = [1] * n, [1] * n, [1] * n
        
        for i in range(1, n):
            l2r[i] = l2r[i-1] * nums[i-1]
            r2l[n-1-i] = r2l[n-i] * nums[n-i]
            
        for i in range(n):
            res[i] = l2r[i]*r2l[i]
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        r = 1
        for i in reversed(range(n-1)):
            r = r * nums[i+1]
            res[i] = res[i] * r
        return res