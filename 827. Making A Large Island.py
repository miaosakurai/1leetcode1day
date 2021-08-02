# 离岛问题
# 先用UnionFind统计一下每个岛的大小，再找0点
# UnionFind总是写错。。
# 这里的UnionFind增加了一个sizes数组，用来记录岛的大小

from collections import namedtuple
from typing import Counter

class UnionFind:
    def __init__(self, n) -> None:
        # parents一维数组，元数据为二维时可以用 row * n + col 压缩到一维
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    # 压缩路径：我parent的parent就是我的parent
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])  # ＼_(・ω・`)ｺｺ重要！
        return self.parents[x]
    
    # x合并到y：x_parent_parent -> y_parent
    # (容易写成 x_parent -> y_parent，这样写的话就会丢失x和x_parent的关联)
    # BEFORE:        |  AFTER:
    # x -> x_parent  |  x -> x_parent -> y_parent
    # y -> y_parent  |              y -> y_parent
    def union(self, x, y):
        p_x, p_y = self.find(x), self.find(y)
        if p_x!=p_y:
            self.sizes[p_y] = self.sizes[p_x] + self.sizes[p_y]
            self.parents[p_x]=p_y   # ＼_(・ω・`)ｺｺ重要！

class Solution:
    def largestIsland(self, grid) -> int:
        res = 0
        N = len(grid)
        uf = UnionFind(N**2)
        for i in range(N):
            for j in range(N):
                if grid[i][j]==0: continue
                cur_id = i*N+j
                nei_ids = self.validNeighborsId(grid, i, j)
                for nei_id in nei_ids:
                    uf.union(cur_id, nei_id)
        
        res = max(uf.sizes)
        
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1: continue
                nei_dir = {}
                nei_ids = self.validNeighborsId(grid, i, j)
                for nei_id in nei_ids:
                    id = uf.find(nei_id)
                    nei_dir[id]=uf.sizes[id]
                new_size = 1
                for k in nei_dir:
                    new_size += nei_dir[k]
                res = max(res, new_size)
        return res
                
    def validNeighborsId(self, grid, i, j):
        N = len(grid)
        neighbors = [[i,j-1], [i, j+1], [i-1, j], [i+1, j]]
        results = []
                
        for nb in neighbors:
            if 0<= nb[0] < N and 0 <= nb[1] < N and grid[nb[0]][nb[1]]==1:
                results.append(nb[0]*N+nb[1])
        return results
                

    def largestIsland_TLE(self, grid) -> int:
        # change every 0 to 1, then get size in that component
        N = len(grid)
        
        def dfs(grid, i, j, visit_matrix):
            visit_matrix[i][j]=1
            count = 1
            # l
            if j<N-1 and visit_matrix[i][j+1]==0 and grid[i][j+1]==1:
                count += dfs(grid, i, j+1, visit_matrix)
            # r
            if j>0 and visit_matrix[i][j-1]==0 and grid[i][j-1]==1:
                count += dfs(grid, i, j-1, visit_matrix)
            # t
            if i>0 and visit_matrix[i-1][j]==0 and grid[i-1][j]==1:
                count += dfs(grid, i-1, j, visit_matrix)
            # b
            if i<N-1 and visit_matrix[i+1][j]==0 and grid[i+1][j]==1:
                count += dfs(grid, i+1, j, visit_matrix)
            return count

        result = 1
        no_zero_found = True
        for i in range(N):
            for j in range(N):
                if grid[i][j]==0:
                    no_zero_found = False
                    visit_matrix = [[0 for i in range(N)] for j in range(N)]
                    count = dfs(grid, i, j, visit_matrix)
                    result = max(result, count)
        if no_zero_found:
            result = N*N
        return result
        
Solution().largestIsland([[1,1],[1,0]])