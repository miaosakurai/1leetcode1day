class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            while len(stack)!=0 and heights[i]<heights[stack[-1]]:
                j = stack.pop()
                if len(stack)==0:
                    cur = heights[j] * (i)
                else:
                    cur = heights[j] * (i-stack[-1]-1)
                res = max(res, cur)
            stack.append(i)
                
        while len(stack)>0:
            j = stack.pop()
            if len(stack)==0:
                cur = heights[j] * len(heights)
            else:
                cur = heights[j] * (len(heights)-stack[-1]-1)
            res = max(res, cur)
            
        return res
            
        
        