class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # for every cell in mxn: if is start point (=1 and left,top!=1)
        # 
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        global_max = 0
        heights = [0 for i in range(n)]
        
        for i in range(m):
            stack = []
            local_max = 0
            for j in range(n):
                # update heights
                if matrix[i][j]=="1":
                    heights[j] += 1
                else:
                    heights[j] = 0
                # largest rectangle in histogram
                if len(stack)==0 or heights[stack[-1]]<=heights[j]:
                    stack.append(j)
                else:
                    while len(stack)!=0 and heights[stack[-1]]>heights[j]:
                        cur_i = stack.pop()
                        if len(stack)==0:
                            cur = heights[cur_i] * (j)
                        else:
                            cur = heights[cur_i] * (j-stack[-1]-1)
                        local_max = max(local_max, cur)
                    stack.append(j)
            while len(stack)>0:
                cur_i = stack.pop()
                if len(stack)==0:
                    cur = heights[cur_i] * (n)
                else:
                    cur = heights[cur_i] * (n-stack[-1]-1)
                local_max = max(local_max, cur)
            global_max = max(global_max, local_max)
        return global_max