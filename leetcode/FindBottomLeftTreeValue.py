# coding:utf-8
"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        q.append(root)
        result = root
        while len(q):
            for i in range(len(q)):
                root = q.popleft()
                if i == 0:
                    result = root
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return result.val










