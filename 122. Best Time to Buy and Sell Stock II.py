## Question
# Buy and Sell Stock and find the maximum profit
# 
# s0: not in transaction
# s1: in transaction
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s0 = 0
        s1 = -prices[0]
        for i in range(1, len(prices)):
            pre_s0, pre_s1 = s0, s1
            s0 = max(pre_s0, pre_s1+prices[i])
            s1 = max(pre_s1, pre_s0-prices[i]) 
        return s0