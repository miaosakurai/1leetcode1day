class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs, top-down dp
        # for each cell, longest=max(top, bottom, left, right)+1
        # T: O(mn), S: O(mn)
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        res = 0
        def find(i, j):
            if dp[i][j]>0: return dp[i][j]
            l = []
            if i>0 and matrix[i-1][j]>matrix[i][j]:
                l.append(find(i-1, j))
            if i<m-1 and matrix[i+1][j]>matrix[i][j]:
                l.append(find(i+1, j))
            if j>0 and matrix[i][j-1]>matrix[i][j]:
                l.append(find(i, j-1))
            if j<n-1 and matrix[i][j+1]>matrix[i][j]:
                l.append(find(i, j+1))
            dp[i][j] = 1 if (len(l)==0) else max(l)+1
            return dp[i][j]
        
        for i in range(m):
            for j in range(n):
                res = max(res, find(i, j))
        return res
        