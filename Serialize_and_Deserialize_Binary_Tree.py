# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        self.serialize_helper(root, data)
        if data:
            return ",".join(map(lambda x: str(x), data))
        else:
            return None

    def serialize_helper(self, node, data):
        if not node:
            return
        if not node.left and not node.right:
            type = 1
        if not node.left and node.right:
            type = 2
        if node.left and not node.right:
            type = 3
        if node.left and node.right:
            type = 4
        data.append(type)
        data.append(node.val)
        if node.left:
            self.serialize_helper(node.left, data)
        if node.right:
            self.serialize_helper(node.right, data)

    def deserialize_helper(self, data):
        if not data:
            return None
        type = int(data.pop(0))
        val = int(data.pop(0))

        node = TreeNode(val)
        if type in [3, 4]:
            node.left = self.deserialize_helper(data)
        if type in [2, 4]:
            node.right = self.deserialize_helper(data)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data_arr = data.split(",")
        ret = self.deserialize_helper(data_arr)
        return ret

# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
codec.deserialize(codec.serialize(root))
