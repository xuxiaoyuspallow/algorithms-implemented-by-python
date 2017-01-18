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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        print(root.val)
        print(root)
        while root:
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)

def tree(r):
    print(r.val)
    while r.left:
        tree(r.left)
        tree(r.right)

if __name__ == '__main__':
    r1 = TreeNode(3)
    r2l = TreeNode(9)
    r2r = TreeNode(20)
    r1.left = r2l
    r1.right = r2r
    r3l = TreeNode(15)
    r3r = TreeNode(7)
    r2r.left = r3l
    r2r.right = r3r
    s = Solution()
    print(s.sumOfLeftLeaves(r1))
    # tree(r1)