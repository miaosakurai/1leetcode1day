class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = len(prices)-1
        res = 0
        
        for i in reversed(range(len(prices)-1)):  # buy
            if prices[i]>prices[sell]:
                sell = i
            else:
                res = max(res, prices[sell]-prices[i])
        return res

    def maxProfit2(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        
        for i in range(1, len(prices)):  # sell
            if prices[i] < prices[buy]:
                buy = i
            else:
                res = max(res, prices[i]-prices[buy])
        return res