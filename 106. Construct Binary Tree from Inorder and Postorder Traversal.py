# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        # preorder: mid, left, right
        # inorder: left, mid, right
        # postorder: left, right, mid
        if len(postorder)==0: return None
        mid_idx = inorder.index(postorder[-1])
        mid = TreeNode(postorder[-1])
        mid.left = self.buildTree(inorder[:mid_idx], postorder[:mid_idx])
        mid.right = self.buildTree(inorder[mid_idx+1:], postorder[mid_idx:len(inorder)-1])
        return mid

Solution().buildTree([9,3,15,20,7],[9,15,7,20,3])