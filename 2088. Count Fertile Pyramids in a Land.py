import numpy as np
class Solution:
    # dp, 很有意思
    def countPyramids(self, grid: List[List[int]]) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        for grid in [grid, grid[::-1]]:
            r = [[-1 for j in range(n)] for i in range(m)]
            def dp(i,j):
                if r[i][j]!=-1:
                    return r[i][j]
                if grid[i][j]==0:
                    r[i][j]=0  # 0层
                    return r[i][j]
                elif i+1>=m or grid[i+1][j]==0:
                    r[i][j]=1  # 1层
                    return r[i][j]

                lb = dp(i+1, j-1) if j>0 else 0
                rb = dp(i+1, j+1) if j<n-1 else 0
                r[i][j] = 1+min(lb, rb)
                return r[i][j]

            for i in range(m):
                for j in range(n):
                    max_p = dp(i,j)
                    if max_p>0:
                        res += max_p-1
        return res
    
    # 类似图像卷积的方法
    def countPyramids_tle(self, grid) -> int:
        res = 0
        m,n = len(grid), len(grid[0])
        a = np.array(grid)
        for s in range(3, n+1, 2):
            k = []
            # s//2+1
            if s//2+1 >m:
                break
            for i in range(s//2+1):
                k.append(i*[0] + (s-2*i)*[1] + i*[0])
            k = np.array(k)
            k_sum = k.sum()
            
            for i in range(m-(s//2+1)+1):
                for j in range(n-s+1):
                    cur_a = a[i:i+(s//2+1)][:, j:j+s]
                    v = cur_a * k
                    inv_v = cur_a * k[::-1]
                    if v.sum() == k_sum:
                        res +=1
                    if inv_v.sum() == k_sum:
                        res +=1
        return res
    
# Solution().countPyramids([
#     [1,1,1,1,0],
#     [1,1,1,1,1],
#     [1,1,1,1,1],
#     [0,1,0,0,1]])

Solution().countPyramids([[0,1,1,0],[1,1,1,1]])