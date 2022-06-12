class KthLargest:
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
        