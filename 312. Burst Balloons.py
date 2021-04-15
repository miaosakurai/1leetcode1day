## Question
# burst all the balloons. Return maximum coins
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
# 边界：*1

# I think they don't really want to hire you if anyone ask you this question during interview (在评论区看到这个有笑到)
# 一开始试图推断出有没有固定的规律（greedy），比如先搞最大值附近的气球，最后越想越复杂，但发现始终有case覆盖不了。
# 看related topic知道要用分治法和dp，但完全不知道如何分治如何dp。毕竟搞了一个气球之后两边的气球之后的值会受影响。。
# 草，写不出来(๑´ㅂ`๑)
# 看到解答之后感觉真的很妙，不是用第一个搞的气球分割，而是用最后一个搞的分割，因为最后一个不会影响前面的结果。
# 
# 思考dp问题的时候往往是从最后一步开始思考，去想最后一步发生的事情+最后一步发生的前置条件。

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # create new nums: add first and last 1 and remove the 0 element.
        arr = [1] + [i for i in nums if i>0] + [1]
        n = len(arr)
        dp = [[0 for j in range(n)] for i in range(n)] # max coins between i and j (excluding i and j)
        for gap in range(2, n):
            for l in range(0, n-gap):
                r = l + gap
                for i in range(l+1, r):  # the last one to burst
                    dp[l][r]=max(dp[l][r], arr[l]*arr[i]*arr[r]+dp[l][i]+dp[i][r])
        return dp[0][n-1]

