class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combine(n, k) = (combine(n-1, k-1) + [n]) + (combine(n-2, k-1) + [n-1]) + ...
        if k==0 or n==0 or n<k:
            return []
        res = []
        if n==k:
            return [[i for i in range(1, n+1)]]
        if k==1:
            for i in range(1, n+1):
                res.append([i])
            return res
        else:
            for i in range(1, n-k+2):
                for l in self.combine(n-i, k-1):
                    l.append(n-i+1)
                    res.append(l)
            return res