## Question
# Buy and Sell Stock and find the maximum profit
# Need to pay fee for every transaction

# Time: O(n), Space: O(1)
# state machine很适合帮助理解这类问题
# s0: not in a transaction
# s1: in a transaction
# s0:rest, s1:sell (and pay) -> s0  (can also pay fee at buy time)
# s1:rest, s0:buy -> s1
# find the maximum of s0

# Greedy, State Machine
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s0 = 0
        s1 = -prices[0]
        
        for i in range(1, len(prices)):
            # get to s0
            pre_s0, pre_s1 = s0, s1
            s0 = max(pre_s0, pre_s1+prices[i]-fee)
            # get to s1
            s1 = max(pre_s1, pre_s0-prices[i])
        return s0     