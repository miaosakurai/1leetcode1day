# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        return self.generateSub(1, n)
        
    def generateSub(self, start, end):
        if start>end: return [None]
        if start==end: return [TreeNode(val=start)]
        res = []
        for i in range(start, end+1):
            l_trees = self.generateSub(start, i-1)
            r_trees = self.generateSub(i+1, end)
            for l in l_trees:
                for r in r_trees:
                    root = TreeNode(val=i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
            
        
Solution().generateTrees(3)