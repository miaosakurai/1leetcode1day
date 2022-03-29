class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(ans, remains):
            if len(remains)==0:
                results.append(ans.copy())
                return
            for i,v in enumerate(remains):
                ans.append(remains.pop(i))
                backtrack(ans, remains)
                remains.insert(i, ans.pop())
        backtrack([], nums)
        return results