from collections import defaultdict

class Solution:
    # for i range from right to left: find leftmost index that can jump to i
    # O(n^2)
    def jump(self, nums) -> int:
        i = len(nums)-1
        step = 0
        while i>0:
            for j in range(i):
                if nums[j]>=i-j:
                    i=j
                    step+=1
                    break
        return step

    # keep a list dict to record index that can achieve key index
    def jump2(self, nums) -> int:
        d = defaultdict(lambda:sys.maxsize)  # input of defaultdict should be function
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                d[i+j] = min(d[i+j], i)
        step = 0
        i = len(nums)-1
        while i>0:
            i = d[i]
            step += 1
        return step

    # bfs
    def jump3(self, nums) -> int:
        step = 0 
        q_start = 0
        q_end = 0
        while q_end < len(nums)-1:
            next_end = q_end
            for i in range(q_start, q_end+1):
                next_end = max(next_end, nums[i]+i)
            q_start = q_end+1
            q_end = next_end
            step +=1
        return step