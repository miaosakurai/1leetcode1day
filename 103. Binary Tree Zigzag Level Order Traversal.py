# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = [root]
        l2r = True
        res = []
        while len(q)>0:
            next_q = []
            cur_res = []
            for i in range(len(q)):
                if q[i].left:
                    next_q.append(q[i].left)
                if q[i].right:
                    next_q.append(q[i].right)
            if not l2r:
                q.reverse()
            for i in range(len(q)):
                cur_res.append(q[i].val)
            res.append(cur_res)
            l2r = not l2r
            q = next_q
        return res
    
    # 优化：遍历时存val，reverse val list
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = [root]
        l2r = True
        res = []
        while len(q)>0:
            next_q = []
            cur_res = []
            for i in range(len(q)):
                cur_res.append(q[i].val)
                if q[i].left:
                    next_q.append(q[i].left)
                if q[i].right:
                    next_q.append(q[i].right)
            if not l2r:
                cur_res.reverse()
            res.append(cur_res)
            l2r = not l2r
            q = next_q
        return res