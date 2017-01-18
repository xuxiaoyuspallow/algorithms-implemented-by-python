"""
           1                                         1
        2      3          ====>                    3     2
      4  5   6  7                               7  6   5  4
"""


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left =None
        self.right = None


def invert_binary_tree_recursive(root):
    if not root:
        return
    left = invert_binary_tree_recursive(root.left)
    right = invert_binary_tree_recursive(root.right)
    root.left,root.right =right,left
    return root



if __name__ == '__main__':
    root = TreeNode(1)
    node1_1 = TreeNode(2)
    node1_2 = TreeNode(3)
    node2_1 = TreeNode(4)
    node2_2 = TreeNode(5)
    node2_3 = TreeNode(6)
    node2_4 = TreeNode(7)
    root.left = node1_1
    root.right = node1_2
    node1_1.left = node2_1
    node1_1.right = node2_2
    node1_2.left = node2_3
    node1_2.right = node2_4
    invert_binary_tree_recursive(root)
    print(root)