class Solution:
    def floodFill_bfs(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs找到所有相连点
        m,n = len(image), len(image[0])
        unvisited = [[True for j in range(n)] for i in range(m)]
        oldColor = image[sr][sc]
        q = [(sr, sc)]
        while len(q)>0:
            next_q = []
            def addPixel(r, c):
                if r>=m or r<0 or c>=n or c<0:
                    return
                if unvisited[r][c] and image[r][c]==oldColor:
                    unvisited[r][c]=False
                    next_q.append((r,c))
            for r,c in q:
                image[r][c] = newColor
                adjs = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                for i,j in adjs:
                    addPixel(i, j)
            q = next_q
            
        return image

    def floodFill_bfs2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 优化bfs
        # - 每层遍历不需要区分，所以不需要两层循环
        # - 函数def写在循环外
        # - 不需要visited，加入了q但pop时已经是newColor的就是visited
        m,n = len(image), len(image[0])
        oldColor = image[sr][sc]
        q = [(sr, sc)]
        def addPixel(r, c):
            if r>=m or r<0 or c>=n or c<0:
                return
            if image[r][c]==oldColor:
                q.append((r,c))
        while len(q)>0:
            r,c = q.pop(0)
            if image[r][c]==newColor:
                continue
            image[r][c] = newColor
            adjs = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for i,j in adjs:
                addPixel(i, j)
        return image


    def floodFill_dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # dfs
        m,n = len(image), len(image[0])
        oldColor = image[sr][sc]
        def dfs(r,c):
            if r>=m or r<0 or c>=n or c<0 or image[r][c]==newColor:
                return
            if image[r][c]==oldColor:
                image[r][c]=newColor
                adjs = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                for i,j in adjs:
                    dfs(i,j)
        dfs(sr, sc)
        return image
        

            

        