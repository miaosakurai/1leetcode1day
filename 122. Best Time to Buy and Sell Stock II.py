## Question
# Buy and Sell Stock and find the maximum profit
# 
# s0: not in transaction
# s1: in transaction
class Solution:
    # 状态机
    def maxProfit(self, prices: List[int]) -> int:
        # i=0时，未持有和持有状态的最大现金
        s0 = 0
        s1 = -prices[0]
        
        for i in range(1, len(prices)):
            next_s1 = max(s1, s0 - prices[i])  # 此时是否买入
            next_s0 = max(s0, s1 + prices[i])  # 此时是否卖出
            s0, s1 = next_s0, next_s1
            
        return s0

    # 每次下降前抛出
    def maxProfit2(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]: # 下降了
                if prices[i-1] > prices[buy]:
                    res += prices[i-1]-prices[buy]
                buy = i
                
        if buy < len(prices)-1:
            res += prices[-1]-prices[buy]
            
        return res