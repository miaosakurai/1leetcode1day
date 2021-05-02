class Solution:
    def lenLongestFibSubseq_bf(self, arr: List[int]) -> int:
        # arr = [1,2,3,4,5,6,7,8]
        # The longest subsequence that is fibonacci-like: [1,2,3,5,8].
        
        # 两两相加，看和在不在arr，在的话继续加 O(n^3)
        d = {}
        for v in arr:
            d[v]=0
        longest = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                cur = 0
                if arr[i]+arr[j] in d:
                    left,right = arr[j],arr[i]+arr[j]
                    cur = 3
                    while left+right in d:
                        left, right = right, left+right
                        cur += 1
                    longest = max(longest, cur)
        return longest

    def lenLongestFibSubseq_dp(self, arr: List[int]) -> int:
        
        # T:O(n^2), S:O(n^2)
        # dp[i][j] = 到arr[i]和arr[j]为止最长的fibonacci-like seq
        # j>i
        #   0 1 2 3
        # 0 * 0 0 0
        # 1 * * 3 3
        # 2 * * * 3
        # 3 * * * *
        # new_i = d[arr[j]-arr[i]]
        # new_j = i
        # if new_i not exsit: dp[i][j] = 0
        # elif new_i>=new_j:  dp[i][j] = 0
        # elif dp[new_i][new_j]==0: dp[i][j] = 3
        # else: dp[i][j] = dp[new_i][new_j]+1
        
        d = {}
        for i,v in enumerate(arr):
            d[v]=i
        longest = 0
        dp = [[0 for j in range(len(arr))] for i in range(len(arr))]
        
        for i in range(1, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j]-arr[i] in d:
                    new_i = d[arr[j]-arr[i]]
                    new_j = i
                    if new_i<new_j:
                        dp[i][j] = dp[new_i][new_j]+1 if dp[new_i][new_j]!=0 else 3
                        longest = max(longest, dp[i][j])
        return longest