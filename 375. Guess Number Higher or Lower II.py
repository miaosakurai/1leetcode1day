## Question
# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
# Input: n = 10
# Output: 16

# dp
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 1-n之间的数，-> n/2 -> 小 -> n/2+n/4 ->...
        # 二分不一定是最优
        # 先遍历每个元素找最优
        # max(min(1:x-1), min(x+1:n))+x 的最小值
        # dp[i][j] = min(i:j)
        dp = [[-1 for j in range(n+1)] for i in range(n+1)]
        for i in range(1,n+1):
            dp[i][i]=0 
            dp[i-1][i]=i-1
        return self.get(1, n, dp)
        
    def get(self, left, right, dp):
        if dp[left][right]!=-1:
            return dp[left][right]
        # right-left>1，min一定不是最左或最右
        for i in range(left+1, right):
            if dp[left][right]==-1:
                dp[left][right] = max(self.get(left, i-1, dp), self.get(i+1, right, dp))+i
            else:
                dp[left][right] = min(dp[left][right], max(self.get(left, i-1, dp), self.get(i+1, right, dp))+i)
        return dp[left][right]
            