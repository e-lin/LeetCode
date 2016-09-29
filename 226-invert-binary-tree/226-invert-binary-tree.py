# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        x = TreeNode(0) # dummy

        if root is not None:
            x = TreeNode(root.val)
        if root is not None and root.right is not None:
            x.left = TreeNode(root.right.val)
            x.left = self.invertTree(root.right)
        if root is not None and root.left is not None:
            x.right = TreeNode(root.left.val)
            x.right = self.invertTree(root.left)

        return x


def printTreeNode(x):
    if x is not None:
        print x.val
    if x is not None and x.left is not None:
        printTreeNode(x.left)
    if x is not None and x.right is not None:
        printTreeNode(x.right)


def main():
    x = TreeNode(4)
    x.left = TreeNode(2)
    x.left.left = TreeNode(1)
    x.left.right = TreeNode(3)

    x.right = TreeNode(7)
    x.right.left = TreeNode(6)
    x.right.right = TreeNode(9)

    # printTreeNode(x)

    solution = Solution()
    result = solution.invertTree(x)
    printTreeNode(result)


if __name__ == '__main__':
    main()