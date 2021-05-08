import collections
## Question
# n个people（1 <= n <= 10），40种帽子。
# Input: hats记录了n个人想带的帽子，e.g. hats = [[3,4],[4,5],[5]]
# Output: 多少种帽子的排列组合分配方法

# bitmask
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10**9 + 7
        who_what_this = collections.defaultdict(list)
        n = len(hats)
        for i in range(n):
            for hat in hats[i]:
                who_what_this[hat].append(i)
        
        dp = [0] * (1<<n)  # n个人戴帽子有(1<<n)种状态
        dp[0] = 1
        for i in who_what_this:
            next_dp = dp.copy()
            for s in range(1<<n):
                for p in who_what_this[i]:
                    if s&(1<<p):  # p在状态s已经有帽子了
                        continue
                    else:  # p在状态s还没有帽子
                        next_dp[s+(1<<p)]+=dp[s]
                        next_dp[s+(1<<p)] %= mod
            dp = next_dp
        return dp[-1]

s = Solution()
s.numberWays([[3,4],[4,5],[5]])