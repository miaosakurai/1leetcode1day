# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### 在每个节点计算：当前子树下的最大双向路径 和 包括当前节点的最大单向路径
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        cur, tot = self.helper(root)
        return tot
    
    def helper(self, root):
        cur, tot, tmp_tot = 0, 0, 0
        if not root:
            return cur, tot
        l_c, l_t = self.helper(root.left)
        r_c, r_t = self.helper(root.right)
        if root.left and root.left.val==root.val:
            cur = 1 + l_c
            tmp_tot = 1 + l_c
        if root.right and root.right.val==root.val:
            cur = max(cur, 1 + r_c)
            tmp_tot += 1 + r_c
        tot = max(tmp_tot, l_t, r_t)
        return cur, tot

    ### 优化：tot_max只需要用一个全局变量维持
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root: return 0
        cur, tmp_tot = 0, 0
        l_c, r_c = self.helper(root.left), self.helper(root.right)
        if root.left and root.left.val==root.val:
            cur = 1 + l_c
            tmp_tot = 1 + l_c
        if root.right and root.right.val==root.val:
            cur = max(cur, 1 + r_c)
            tmp_tot += 1 + r_c
        self.res = max(tmp_tot, self.res)
        return cur