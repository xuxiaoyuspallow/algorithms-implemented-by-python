"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    r = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # print(root.val)
        while root:
            if root.left:
                if not root.left.left and not root.left.right:
                    self.r += root.left.val
                self.sumOfLeftLeaves(root.left)
            if root.right:
                self.sumOfLeftLeaves(root.right)
            break
        return self.r
