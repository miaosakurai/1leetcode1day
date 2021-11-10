class Solution:
    def longestWPI_tle(self, hours) -> int:
        # tiring day: hours[i]>8
        res = 0
        n = len(hours)
        for i in range(n):
            tiring, non_tiring = 0, 0
            for j in range(i, n):
                if hours[j]>8:
                    tiring += 1
                else:
                    non_tiring += 1
                if tiring > non_tiring:
                    res = max(res, j-i+1)
        return res

    def longestWPI2(self, hours) -> int:
        # 参考大佬的答案 https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/JavaC%2B%2BPython-O(N)-Solution-Life-needs-996-and-669
        # 用 s_i - s_j 求 j~i 
        res, score = 0, 0
        seen = {}
        # seen[s] = p (首次出现score的potision)
        for i, h in enumerate(hours):
            score = score + 1 if h>8 else score-1
            if score > 0:
                res = i+1
            seen.setdefault(score, i)
            if score-1 in seen:  # 说明(seen[score-1], i] 之间的score>=1
                res = max(res, i-seen[score-1])

        return res

Solution().longestWPI2([9,9,6,0,6,6,9])
