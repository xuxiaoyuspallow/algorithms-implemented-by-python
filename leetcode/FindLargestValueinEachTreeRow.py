# coding:utf-8
"""

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        tree, result = [], []
        tree.append(root)
        while len(tree):
            temp = []
            for i in range(len(tree)):
                r = tree.pop(0)
                temp.append(r.val)
                if r.left:
                    tree.append(r.left)
                if r.right:
                    tree.append(r.right)
            result.append(max(temp))
        return result
