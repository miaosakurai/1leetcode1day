# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 设计二叉树的序列化和反序列化
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # [1,[2,[],[]],[3,[4,[],[]],[5,[],[]]]]
        if root is None:
            return "[]"
        return "[" + ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)]) + "]"
    
    def splitter(self, data):
        i=1
        while data[i]!=",":
            i+=1
        val = int(data[1:i]) # i: ","
        
        # left
        i += 1 # i: "["
        start = i
        count=1
        while count>0:
            i+=1
            if data[i]=="[":
                count+=1
            if data[i]=="]":
                count-=1
        left = data[start:i+1]
        right = data[i+2:-1]
        return val, left, right
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]": return None
        val, l, r = self.splitter(data)
        root = TreeNode(val)
        root.left = self.deserialize(l)
        root.right = self.deserialize(r)
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))