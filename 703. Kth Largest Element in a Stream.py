# 1. first solution
class KthLargest1:
    def __init__(self, k: int, nums: List[int]):
        self.topk = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        i = len(self.topk)-1
        while i>=0 and val > self.topk[i]:
            i-=1
        self.topk.insert(i+1, val)
        self.topk = self.topk[:self.k]
        return self.topk[-1]


# 2. priority queue, heap
import heapq

class KthLargest:
    # O(n*logn)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) # O(n)
        for i in range(len(self.heap)-k): # O(n*logn)
            heapq.heappop(self.heap)

    # O(logk)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # O(logk)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)