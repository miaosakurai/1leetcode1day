# Last Stone Weight II
# 两个石头相撞，小石头消失，大石头重量=大石头-小石头
# 相等则两个石头都消失
# 最后最多剩下一个，返回剩下的那个重量最小值，一个都不剩返回0
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100

# 问题可以转换为：用这些weight加加减减，得到的大于零的最小值是多少。
class Solution:
    # # BF：每个weight是加还是减，复杂度O(2^n)，stones.length <= 30
    # TLE O(2^n)
    def lastStoneWeightII_bf(self, stones: List[int]) -> int:
        n = len(stones)
        res = sum(stones)
        for i in range(2 ** n):
            cur = 0
            for j in range(n):
                if (2 ** j) & i > 0:
                    cur += stones[j]
                else:
                    cur -= stones[j]
            if cur >= 0:
                res = min(res, cur)
        return res

    # 用set存到当前stones[i]为止所有可能的结果，最后求大于零的最小值。
    # （用set就AC，用list就TLE了，用set去重之后复杂度最差还是O(2^n)呀.. -> 由约束条件可知可能结果值范围[-3000, 3000], 所以去重后可以保证不会超时）
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 0: return 0

        s_pre = {stones[0], -stones[0]}
        s = set()
        for i in range(1, n):
            s = set()
            for v in s_pre:
                s.add(v - stones[i])
                s.add(v + stones[i])
            s_pre = s

        res = sum(stones)
        for i in s:
            if i >= 0:
                res = min(res, i)
        return res

    # 可能结果里不存负值（改存绝对值）
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 0: return 0

        s = {stones[0]}
        s_pre = s
        for i in range(1, n):
            s = set()
            for v in s_pre:
                s.add(abs(v - stones[i]))
                s.add(v + stones[i])
            s_pre = s

        return min(s)

    # 参考https://leetcode.com/problems/last-stone-weight-ii/discuss/294888/JavaC%2B%2BPython-Easy-Knapsacks-DP
    # 用comprehension的写法
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}  # achievable result, 初始是0因为还没有开始遍历
        for i in range(len(stones)):
            # set a,b求并集：a | b
            dp = {stones[i]+v for v in dp} | {abs(stones[i]-v) for v in dp}
        return min(dp)