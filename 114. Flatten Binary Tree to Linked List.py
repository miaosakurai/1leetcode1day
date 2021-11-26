# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root):
        if not root:
            return None, None
        l, r = root.left, root.right
        if not l and not r:
            return root, root
        elif not l:
            root.right, r_last = self.helper(r)
            root.left = None
            return root, r_last
        else:
            root.right, l_last = self.helper(l)
            root.left = None
            if r:
                l_last.right, r_last = self.helper(r)
                return root, r_last
            else:
                return root, l_last