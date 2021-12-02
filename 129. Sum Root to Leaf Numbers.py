# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(map(int, self.dfs(root)))
        
    def dfs(self, root):
        l = []
        if root is None:
            return l
        if not root.left and not root.right:
            return [str(root.val)]
        for s in self.dfs(root.left) + self.dfs(root.right):
            l.append(str(root.val) + s)
        return l

    # 一个小坑：如果用数字计算，连0的部分没法保留
    # def dfs(self, root):
    #     l = []
    #     if root is None:
    #         return l
    #     if not root.left and not root.right:
    #         print(root.val)
    #         return [root.val]
    #     for num in self.dfs(root.left):
    #         l.append(root.val * (10**len(str(num))) + num)
    #     for num in self.dfs(root.right):
    #         l.append(root.val * (10**len(str(num))) + num)
    #     return l