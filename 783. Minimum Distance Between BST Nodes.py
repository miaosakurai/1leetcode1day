# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l = self.preorder(root)
        res = abs(l[1]-l[0])
        for i in range(2, len(l)):
            res = min(res, abs(l[i]-l[i-1]))
        return res
    
    def preorder(self, root):
        if root is None: return []
        return self.preorder(root.left) + [root.val] + self.preorder(root.right)
        
# 参考
class Solution:
    pre = -float(inf)
    res = float(inf)
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.preorder(root)
        return self.res
    
    def preorder(self, root):
        if root.left:
            self.preorder(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.preorder(root.right)