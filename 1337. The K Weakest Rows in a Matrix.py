class Solution:
    # Approach 1. sorting 
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

    # Approach 2. use dict instead of sorting
    def kWeakestRows2(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            d[sum(mat[i])].append(i)
        
        res = []
        for i in range(n+1):
            for v in d[i]:
                res.append(v)
            if len(res)>=k:
                return res[:k]
        return res[:k]