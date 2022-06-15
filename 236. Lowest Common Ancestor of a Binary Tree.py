# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # A1: find path for p and q, compare 2 pathes
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_p = self.path(root, p)
        q_p = self.path(root, q)
        n = min(len(p_p), len(q_p))
        for i in range(n):
            if p_p[i].val != q_p[i].val:
                return p_p[i-1]
        return p_p[n-1]
    
    def path(self, r, e):
        if not r:
            return []
        p = [r]
        if r.val==e.val:
            return p
        lp = self.path(r.left, e)
        if lp and len(lp)>0 and lp[-1].val == e.val:
            return p+lp
        rp = self.path(r.right, e)
        if rp and len(rp)>0 and rp[-1].val == e.val:
            return p+rp
            
    # A2: recursion 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # postorder 
        # not None if one of p,q is in current tree
        if not root: return None
        if root.val==p.val or root.val==q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
            
        if left and right:  # found both side -> p,q are in l,r tree
            return root
        elif left:
            return left
        else:
            return right
            
            