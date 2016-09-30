# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        x = TreeNode(0) # dummy

        if root is not None:
            x = TreeNode(root.val)
        if root.right is not None:
            x.left = TreeNode(root.right.val)
            x.left = self.invertTree(root.right)
        if root.left is not None:
            x.right = TreeNode(root.left.val)
            x.right = self.invertTree(root.left)

        return x

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.isSameTree(root, self.invertTree(root))


def printTree(x):
    if x is not None:
        print x.val
    if x.left is not None:
        printTree(x.left)
    if x.right is not None:
        printTree(x.right)


def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)

    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)
    # printTree(root)
    root = None

    solution = Solution()
    print solution.isSymmetric(root)


if __name__ == '__main__':
    main()