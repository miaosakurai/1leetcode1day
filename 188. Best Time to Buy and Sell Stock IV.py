class Solution:
    # prices[i]: the price of a given stock on the ith day
    # at most k transaction
    
    # TLE
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<2: return 0
        
        n = len(prices)
        dp = [[0 for i in range(n)] for i in range(k+1)]
        
        for i in range(1, k+1):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # day j卖出, day l 买入
                for l in range(j):
                    if l>1:
                        dp[i][j] = max(dp[i][j], dp[i-1][l-1]+prices[j]-prices[l])
                    else:
                        dp[i][j] = max(dp[i][j], prices[j]-prices[l])
        
        return dp[k][n-1]

    # 局部用状态机求dp[i][j]，不需要双重循环
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<2: return 0
        
        n = len(prices)
        dp = [[0 for i in range(n)] for i in range(k+1)]
        
        for i in range(1, k+1):
            # dp[i][j] = 0 # 未持有
            s1 = -prices[0] # 持有
            for j in range(1, n): # day j卖出
                dp[i][j] = max(dp[i][j-1], s1+prices[j])  # 是否在day j卖出
                s1 = max(s1, dp[i-1][j-1]-prices[j])  # 是否在day j买入
        
        return dp[k][n-1]