# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 子问题：经过节点的最大单条路径 (subp)
        # res = max(通过当前节点mps, 通过左节点mps，通过右节点mps)
        # mps = l.subp + cur.val + r.subp
        # Note: subp可能为负，必须是non-empty path
        
        def maxSubPathSum(root):
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return root.val, root.val
            l_subp, l_p = maxSubPathSum(root.left)
            r_subp, r_p = maxSubPathSum(root.right)
            subp, p = root.val, root.val+max(l_subp,0)+max(r_subp,0)
            if root.left:
                subp = max(subp, root.val+l_subp)  # subp可能为负
                p = max(p, l_p)
            if root.right:
                subp = max(subp, root.val+r_subp)  # subp可能为负
                p = max(p, r_p)

            return subp, p
        
        subp, p = maxSubPathSum(root)
        return p

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        # global记录mps，递归返回subp
        self.res = float('-inf')
        
        def maxSubPathSum(root):
            if not root: return 0
            l_subp = max(0, maxSubPathSum(root.left))
            r_subp = max(0, maxSubPathSum(root.right))
            self.res = max(self.res, l_subp+r_subp+root.val)  # 经过当前节点的mps
            return root.val + max(l_subp, r_subp) # 经过当前节点的subp
        
        maxSubPathSum(root)
        return self.res