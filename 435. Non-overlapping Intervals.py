'''
最大不重叠间隔问题
greedy: 每次选择最早结束的间隔，就能得到最多间隔数

'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        count = 1
        for s, e in intervals[1:]:
            if s>=end:
                end = e
                count +=1
        return len(intervals)-count
        