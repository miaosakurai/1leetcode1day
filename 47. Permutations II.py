class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. recursion
        nums.sort()
        if len(nums)==1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for l in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+l)
        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        # 2. backtrack
        results = []
        def backtrack(ans, c):
            if len(ans)==len(nums):
                results.append(list(ans))
                return
            for k in c:
                if c[k]>0:
                    c[k]-=1
                    ans.append(k)
                    backtrack(ans, c)
                    ans.pop()
                    c[k]+=1
        backtrack([], Counter(nums))
        return results

    def permuteUnique3(self, nums):
        # https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
        # bottom up生成
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break
            ans = new_ans
        return ans