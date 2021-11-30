class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    uf.count+=1
                    if i>0 and grid[i-1][j]=="1":
                        uf.union(n*i+j, n*(i-1)+j)
                    if j>0 and grid[i][j-1]=="1":
                        uf.union(n*i+j, n*i+j-1)
        return uf.count
        
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.count = 0
        
    def find(self, x):
        if x!=self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x!=y:
            self.count-=1
            self.par[x]=y
        