# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deep(self, root):
        if not root:
            return 0
        if root.left:
            l_res = self.deep(root.left)
        if root.right:
            r_res = self.deep(root.right)
        if r_res == -1 and l_res == -1 and abs(l_res - r_res) > 1:
            return -1
        else:
            return max(r_res,l_res)+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.deep(root)
        if res:
            return True
        else:
            return res
