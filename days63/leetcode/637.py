# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    queue = [root]
    res = []
    while queue[0]:
        val = []
        index = len(queue)
        for i in range(index):
            node = queue.pop(0)
            val.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        avg=sum(val)/len(val)
        res.append(avg)
    return res