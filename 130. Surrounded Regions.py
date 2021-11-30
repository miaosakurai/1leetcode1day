class Solution:
    # 1. union-find
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        uf = UF(m*n)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if i==0 or j==0 or i==m-1 or j==n-1:
                        uf.setSur(n*i+j)
                    if i>0 and board[i-1][j]=='O':
                        uf.union(n*i+j, n*(i-1)+j)
                    if j>0 and board[i][j-1]=='O':
                        uf.union(n*i+j, n*i+j-1)
        # find not surrounded
        for i in range(m):
            for j in range(n):
                if uf.getSur(n*i+j):
                    board[i][j]='X'
        
class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sur = [True for i in range(n)]
    
    def setSur(self, x):
        self.sur[x] = False
    
    def getSur(self, x):
        self.parents[x] = self.find(x)
        return self.sur[self.parents[x]]
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if not self.sur[x] or not self.sur[y]:
            self.sur[x], self.sur[y] = False, False
        self.parents[x] = y
        
    def find(self, x):
        if self.parents[x]!=x:
            if not self.sur[x] or not self.sur[self.parents[x]]:
                self.sur[x], self.sur[self.parents[x]] = False, False
            self.parents[x] = self.find(self.parents[x])
        self.sur[x] = self.sur[self.parents[x]]
        return self.parents[x]


# 2: dfs start from every boundary "O"
    def solve_dfs(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # set not surrounded region as "A"
        def dfs(i, j):
            board[i][j] = 'A'
            if j>0 and board[i][j-1]=='O':
                dfs(i, j-1)
            if j<n-1 and board[i][j+1]=='O':
                dfs(i, j+1)
            if i>0 and board[i-1][j]=='O':
                dfs(i-1, j)
            if i<m-1 and board[i+1][j]=='O':
                dfs(i+1, j)
        
        for i in range(m): # left and right
            if board[i][0]=='O':
                dfs(i, 0)
            if board[i][n-1]=='O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j]=='O':
                dfs(0, j)
            if board[m-1][j]=='O':
                dfs(m-1, j)
        # O->X, A->O
        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if board[i][j] in 'XO' else 'O'
        
                

            
