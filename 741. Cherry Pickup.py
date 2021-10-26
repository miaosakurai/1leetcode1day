class Solution:
    # first idea (WA): 计算第一次dp最大值，把路径上的1->0，再计算第二次
    # problem: 第一次取最大值不能保证全局最大，e.g:
    #[[1,1,1,0,1],
    # [0,0,0,0,0],
    # [0,0,0,0,0],

    # [0,0,0,0,0],
    # [1,0,1,1,1]].

    def cherryPickup_wa(self, grid) -> int:
        n = len(grid)
        dp = [[0] * (n+1) for i in range(n+1)]
        dp_idx = [[[] for i in range(n+1)] for i in range(n+1)]
        
        # need path record for second round
        for i in range(1, n+1):
            for j in range(1, n+1):
                if grid[i-1][j-1]==-1:
                    continue
                if dp[i-1][j]<dp[i][j-1]:
                    dp_idx[i][j] = dp_idx[i][j-1] + [(i,j)]
                    dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
                else:
                    dp_idx[i][j] = dp_idx[i-1][j] + [(i,j)]
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
        
        if dp[n][n] == 0: return 0
        first = dp[n][n]
        for idx in dp_idx[n][n]:
            if grid[idx[0]][idx[1]]==1:
                grid[idx[0]][idx[1]] = 0
                
        # second round
        dp = [[0] * (n+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if grid[i-1][j-1]==-1:
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[n][n]+first
                    
        
    # 需要minimize overlap
    # second idea: 记录所有可以通过的非零的path，两两计算总和-overlap，取最大
    def cherryPickup_tle(self, grid) -> int:
        n = len(grid)
        
        dp = [[0] * (n+1) for i in range(n+1)]
        dp_idx = [[[] for i in range(n+1)] for i in range(n+1)]
        
        # need path record for second round
        # only add cherry in path
        for i in range(1, n+1):
            for j in range(1, n+1):
                if grid[i-1][j-1]==-1 or (dp[i-1][j]==-1 and dp[i][j-1]==-1) or (i==1 and dp[i][j-1]==-1) or (j==1 and dp[i-1][j]==-1):
                    dp[i][j]=-1
                elif grid[i-1][j-1]==1:
                    if len(dp_idx[i][j-1])!=0:
                        dp_idx[i][j] += [path+[(i-1)*n+j-1] for path in dp_idx[i][j-1]]
                    if len(dp_idx[i-1][j])!=0:
                        dp_idx[i][j] += [path+[(i-1)*n+j-1] for path in dp_idx[i-1][j]]
                    if len(dp_idx[i][j])==0:
                        dp_idx[i][j] = [[(i-1)*n+j-1]]
                else:
                    if dp[i][j-1]!=-1:
                        dp_idx[i][j] += dp_idx[i][j-1]
                    if dp[i-1][j]!=-1:
                        dp_idx[i][j] += dp_idx[i-1][j]
        
        # for every two paths, compute total
        paths = dp_idx[n][n]
        if len(paths)==0: return 0
        if len(paths)==1: return len(paths[0])
        res = 0

        print(paths)

        # TLE
        def get_total(l1, l2):
            return len(set(l1+l2))
        for i in range(len(paths)):
            for j in range(i+1, len(paths)):
                res = max(res, get_total(paths[i], paths[j]))
        
        return res
     
                
# 1,3,6,7,8
# Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]])
# Solution().cherryPickup([[1,1,1,1,-1,-1,-1,1,0,0],[1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,1,1,1,0,-1,1,1],[0,0,0,0,1,-1,0,0,1,-1],[1,0,1,1,1,0,0,-1,1,0],[1,1,0,1,0,0,1,0,1,-1],[1,-1,0,1,0,0,0,1,-1,1],[1,0,-1,0,-1,0,0,1,0,0],[0,0,-1,0,1,0,1,0,0,1]])


    # 三维dp，两个人同时走两条线路，分别位于(r1,c1),(r2,c2)
    # 因为r1+c1==r2+c2，确定r1,c1,r2即可
    #  dp[r1][c1][r2] = total
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[0] * n for i in range(n)] for i in range(n)]
        dp[0][0][0] = grid[0][0]
        for r1 in range(n):
            for c1 in range(n):
                for r2 in range(n):
                    if r1+c1-r2 not in range(n):
                        dp[r1][c1][r2]=-1  # invalid
                        continue
                    if grid[r1][c1]==-1 or grid[r2][r1+c1-r2]==-1:
                        dp[r1][c1][r2]=-1  # invalid
                        continue
                    if r1==0 and c1==0 and r2==0:
                        continue
                    pres = []
                    if r1>=1:
                        if r1+c1-r2>=1 and dp[r1-1][c1][r2]!=-1:
                            pres.append(dp[r1-1][c1][r2])
                        if r2>=1 and dp[r1-1][c1][r2-1]!=-1:
                            pres.append(dp[r1-1][c1][r2-1])
                    if c1>=1:
                        if r1+c1-r2>=1 and dp[r1][c1-1][r2]!=-1:
                            pres.append(dp[r1][c1-1][r2])
                        if r2>=1 and dp[r1][c1-1][r2-1]!=-1:
                            pres.append(dp[r1][c1-1][r2-1])
                    if len(pres)==0:
                        dp[r1][c1][r2]=-1  # invalid
                        continue
                    cur = 0
                    if r1==r2:
                        cur = grid[r1][c1]
                    else:
                        cur = grid[r1][c1] + grid[r2][r1+c1-r2]
                    
                    dp[r1][c1][r2] = max(pres) + cur
        return 0 if dp[n-1][n-1][n-1]==-1 else dp[n-1][n-1][n-1]
                    