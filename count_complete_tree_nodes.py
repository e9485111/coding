# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def leftheight(self,root):
      if not root:
        return 0
      if not (root.left or root.right):
        return 1
      else:
        return 1+self.leftheight(root.left)

    def rightheight(self,root):
      if not root:
        return 0
      if not (root.left or root.right):
        return 1
      else:
        return 1+self.rightheight(root.right)

    def countNodes(self, root):
      if not root:
        return 0
      elif not (root.left or root.right):
        return 1
      else:
        l = self.leftheight(root)
        r = self.rightheight(root)
        if l == r:
          return pow(2,l)-1
        else:
          return 1+ self.countNodes(root.left) + self.countNodes(root.right)

