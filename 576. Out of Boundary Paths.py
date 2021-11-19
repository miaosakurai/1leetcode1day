class Solution:
    # TLE：直接递归
    def findPaths_tle(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # out of matrix
        res = 0
        for i in range(maxMove):
            res += self.find(m, n, i, startRow+1, startColumn) \
            + self.find(m, n, i, startRow-1, startColumn) \
            + self.find(m, n, i, startRow, startColumn+1) \
            + self.find(m, n, i, startRow, startColumn-1)
        return res

    def find(self, m, n, move, r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            if move == 0:
                return 1
            else:
                return 0
        elif move == 0:
            return 0
        res = 0
        return self.find(m, n, move-1, r+1, c) \
            + self.find(m, n, move-1, r-1, c) \
            + self.find(m, n, move-1, r, c+1) \
            + self.find(m, n, move-1, r, c-1)


    def __init__(self):
        self.dp = [[[-1 for i in range(50)] for j in range(50)] for k in range(50)]
        
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # out of matrix
        res = 0
        for i in range(maxMove):
            res += self.find(m, n, i, startRow+1, startColumn) \
            + self.find(m, n, i, startRow-1, startColumn) \
            + self.find(m, n, i, startRow, startColumn+1) \
            + self.find(m, n, i, startRow, startColumn-1)
        return res % (10**9+7)

    def find(self, m, n, move, r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            if move == 0:
                return 1
            else:
                return 0
        elif move == 0:
            return 0
        if self.dp[r][c][move] == -1:
            self.dp[r][c][move] = self.find(m, n, move-1, r+1, c) \
                + self.find(m, n, move-1, r-1, c) \
                + self.find(m, n, move-1, r, c+1) \
                + self.find(m, n, move-1, r, c-1)
        return self.dp[r][c][move]

print(Solution().findPaths(1,3,3,0,1))