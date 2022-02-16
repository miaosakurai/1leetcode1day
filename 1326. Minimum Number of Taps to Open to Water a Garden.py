class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # select from max range? x
        # sort taps by start point
        # select tap in cur range with max end point
        # 最小间隔数问题
        taps = [[i-ranges[i], i+ranges[i]] for i in range(n+1)]
        taps.sort()
        start = 0
        res = 0
        # print(taps)
        while len(taps)>0 and start<n:
            cur_max = start
            while len(taps)>0 and taps[0][0]<=start:
                cur_max = max(cur_max, taps.pop(0)[1])  # find max end
            if cur_max <= start: 
                return -1
            print(cur_max)
            start = cur_max
            res += 1
            
        return res
        