class Solution:
    def characterReplacement(self, s, k):
        # 参考：https://leetcode.com/problems/longest-repeating-character-replacement/discuss/278271/JavaC%2B%2BPython-Sliding-Window-just-O(n)
        # sliding window
        # max_window: 最大窗口
        # 每次把i加入窗口：
        # 能扩展：extend max_window
        # 不能扩展：move max_window
        
        max_count, max_window = 0, 0
        counter = collections.Counter()
        
        for i in range(len(s)):
            counter[s[i]] += 1
            max_count = max(max_count, counter[s[i]])
            if max_window - max_count < k: # 能扩展的条件：需要修改的字母数<=k
                max_window += 1  # extend max_window
            else:
                counter[s[i - max_window]] -= 1
        return max_window