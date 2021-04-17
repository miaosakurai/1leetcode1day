## Question
# Buy and Sell Stock and find the maximum profit  
# After you sell your stock, you CANNOT buy stock on the NEXT DAY

# Time: O(n), Space: O(1)
# 有多种状态的时候可以画个状态机图
#
# s0: 未买入且非冷静期，buy->s1 / rest->s0
# s1: 以买入，sell->s2 / rest->s1
# s2: 冷静期，rest->s0
# 每个状态记录当前最大现金数
# find maximum of s0 and s2
# ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0
        s0 = 0
        s1 = -prices[0]
        s2 = 0
        for i in range(1, len(prices)):
            pre_s0, pre_s1, pre_s2 = s0, s1, s2  # 滚动变量代替一维数组
            s0 = max(pre_s0, pre_s2)  # s0->rest / s2->rest
            s1 = max(pre_s1, pre_s0-prices[i]) # s1->rest / s0->buy
            s2 = pre_s1+prices[i] # s1->sell
        return max(s0, s2)
            
            
            