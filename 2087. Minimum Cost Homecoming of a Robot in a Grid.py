class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        row, col = 0, 0
        if startPos[0]<=homePos[0]:
            row = sum(rowCosts[startPos[0]+1:homePos[0]+1])
        else:
            row = sum(rowCosts[homePos[0]:startPos[0]])
        if startPos[1]<=homePos[1]:
            col = sum(colCosts[startPos[1]+1:homePos[1]+1])
        else:
            col = sum(colCosts[homePos[1]:startPos[1]])
        return row+col