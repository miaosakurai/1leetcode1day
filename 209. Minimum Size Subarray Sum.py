class Solution:
    def minSubArrayLen_bf1(self, target: int, nums: List[int]) -> int:
        # bf: O(n^3) for start, for size, sum
        # TLE
        n = len(nums)
        if sum(nums)<target: return 0
        for l in range(1, n):
            for start in range(n-l+1):
                if sum(nums[start:start+l])>=target:
                    return l
        return n

    def minSubArrayLen_bf2(self, target: int, nums: List[int]) -> int:
        # bf: O(n^2) sum->O(1)
        n = len(nums)
        sums = [0] * (n+1)  # sum before i
        for i in range(1, n+1):
            sums[i] = sums[i-1]+nums[i-1]
        
        if sums[n]<target: return 0
        for l in range(1, n):
            for start in range(n-l+1):
                if sums[start+l]-sums[start]>=target:
                    return l
        return n

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 pointers
        n = len(nums)
        sums = [0] * (n+1)  # sum before i
        for i in range(1, n+1):
            sums[i] = sums[i-1]+nums[i-1]
        
        if sums[n]<target: return 0
        l, r, res = 0, 1, n
        while r<n+1:
            while r<n+1 and sums[r]-sums[l]<target:
                r+=1
            if r<n+1:
                res = min(res, r-l)
                while l<n and sums[r]-sums[l]>=target:
                    l+=1
                if l<n+1:
                    res = min(res, r-l+1)
        return res