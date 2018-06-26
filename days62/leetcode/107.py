# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfst(self, queue):

        child_queue = []
        node_list = []
        res_list = []
        for i in range(len(queue)):
            if queue[i]:
                print('in  for', queue[i])
                node_list.append(queue[i].val)
                child_queue.append(queue[i].left)
                child_queue.append(queue[i].right)

        # print('===child_queue==',child_queue)

        if child_queue == []:
            return

        res = self.bfst(child_queue)
        if res:
            res_list.extend(res)
        # print('===res_list 2==',res_list)

        res_list.append(node_list)
        # print('===res_list 1==',res_list)
        return res_list

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = []
        queue.append(root)
        res = self.bfst(queue)
        if not res:
            return []
        return res

