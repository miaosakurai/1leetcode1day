# 离岛问题
# 先用UnionFind统计一下每个岛的大小，再找0点
# UnionFind总是写错。。
# 这里的UnionFind增加了一个sizes，用来记录岛的大小，相应地增加一个add函数用于初始化值为1的“新岛”

from collections import namedtuple
from typing import Counter

class UnionFind:
    def __init__(self, n) -> None:
        # parents一维数组，元数据为二维时可以用 row * n + col 压缩到一维
        self.parents = [i for i in range(n)]
        self.sizes = [0 for i in range(n)]

    def add(self, x):
        if self.sizes[x]==0:
            self.sizes[x]=1

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
            new_size = self.sizes[p_x] + self.sizes[p_y]
            self.parents[p_x]=p_y  # ＼_(・ω・`)ｺｺ重要！
            self.sizes[p_y] = new_size

class Solution:
    def largestIsland(self, grid) -> int:
        res = 0
        N = len(grid)
        uf = UnionFind(N**2)
        for i in range(N):
            for j in range(N):
                if grid[i][j]==0: continue
                cur_id = i*N+j
                uf.add(cur_id)
                neighbors = self.validNeighbors(grid, i, j)
                for nb in neighbors:
                    nei_id = nb[0]*N+nb[1]
                    uf.add(nei_id)
                    uf.union(cur_id, nei_id)
                print(uf.find(cur_id))
                res = max(res, uf.sizes[uf.find(cur_id)])
        
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1: continue
                nei_dir = {}
                neighbors = self.validNeighbors(grid, i, j)
                for nb in neighbors:
                    id = uf.find(nb[0]*N+nb[1])
                    nei_dir[id]=uf.sizes[id]
                new_size = 1
                for k in nei_dir:
                    new_size += nei_dir[k]
                res = max(res, new_size)
        return res
                
    def validNeighbors(self, grid, i, j):
        neighbors = [[i,j-1], [i, j+1], [i-1, j], [i+1, j]]
        results = []
        for n in neighbors:
            if 0<= n[0] < len(grid) and 0 <= n[1] < len(grid) and grid[n[0]][n[1]]==1:
                results.append(n)
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