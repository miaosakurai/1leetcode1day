# Minimum ASCII Delete Sum for Two Strings
# 删除ASCII和最小的字母，使s1和s2剩余部分的字符串相等

# a=101, z=132, 两个字母一定比一个字母大，所以尽量少删，删的相等时再选删的小的
# 尽量保留更长，相等时选择字符更大的。-> 最长公共子序列，选择子问题时加一个条件就行了
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]: [length, ASCII_sum]
        dp = [[[0, 0] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]).copy()
                # equal char found
                if s1[i - 1] == s2[j - 1]:
                    if dp[i - 1][j - 1][0] + 1 > dp[i][j][0]:
                        dp[i][j][0] = dp[i - 1][j - 1][0] + 1
                        dp[i][j][1] = dp[i - 1][j - 1][1] + ord(s1[i - 1])
                    elif dp[i - 1][j - 1][0] + 1 == dp[i][j][0]:
                        dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][1] + ord(s1[i - 1]))
        return self.asciiSum(s1) + self.asciiSum(s2) - 2 * dp[len(s1)][len(s2)][1]

    # 发现其实只存当前ASCII和就好了。
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]: ASCII_sum
        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # equal char found
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + ord(s1[i - 1]))
        return self.asciiSum(s1) + self.asciiSum(s2) - 2 * dp[len(s1)][len(s2)]

    def asciiSum(self, s: str):
        res = 0
        for c in s:
            res += ord(c)
        return res

