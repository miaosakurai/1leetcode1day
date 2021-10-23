import heapq  
import bisect  # 二分查找 https://docs.python.org/zh-cn/3.6/library/bisect.html

# 这个题目是不是有点问题，按照规则最后的可能结果应该是唯一的，为什么问的是smallest possible weight
class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort()
        n = len(stones)
        
        while len(stones)>1:
            x = stones[-1]
            y = stones[-2]
            if x==y:
                stones = stones[:-2]
            else:
                stones = stones[:-2]
                stones.append(abs(y-x))
                stones.sort()  # 待优化
        return 0 if len(stones)==0 else stones[0]


    def lastStoneWeight2(self, stones) -> int:
        stones.sort()
        n = len(stones)
        
        while len(stones)>1:
            x = stones[-1]
            y = stones[-2]
            if x==y:
                stones = stones[:-2]
            else:
                stones = stones[:-2]
                bisect.insort(stones, x-y)  # 数组二分查找

        return 0 if len(stones)==0 else stones[0]
        
    # 优化：优先队列 heapq
    # 参考：https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue
    def lastStoneWeight3(self, stones) -> int:
        
        q = [-s for s in stones]
        heapq.heapify(q)  # Note: heapq.heapify(q)修改q，不返回值
        # O(n),heapq.heapify()只支持最小堆，所以通过存负值实现最大堆 
        
        while len(q)>1 and q[0]!=0:
            item = heapq.heappop(q)-heapq.heappop(q)  # 取出两个最大值
            heapq.heappush(q, item)

        return -q[0]