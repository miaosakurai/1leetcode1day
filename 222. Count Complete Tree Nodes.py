## Question
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# 
import TreeNode

class Solution:
    # Traverse all nodes: O(n)
    def countNodesV1(self, root: TreeNode) -> int:
        if root is None: return 0
        else: return self.countNodes(root.right)+self.countNodes(root.left)+1

    # complete binary tree: full before the last node.
    # compare depth between left and right subtree:
    # if left_depth==right_depth: left is full, left_count=2^left_depth-1
    # else: right is full, right_count = 2^right_depth-1
    # O(logn*logn)  # countNodes * getDepth
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if left_depth==right_depth:  # left is full
            return self.countNodes(root.right)+pow(2, left_depth)
        else:
            return self.countNodes(root.left)+pow(2, right_depth)
    
    # get complete binary tree depth: get leftmost node
    def getDepth(self, root):
        if root is None: return 0
        return self.getDepth(root.left)+1

    # ref: https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
    
