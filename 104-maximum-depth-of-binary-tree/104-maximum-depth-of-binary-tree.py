# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _level(root, level):
            if root is None:
                return
            else:
                d[level] = d.get(level, []) + [root.val]
                # print root.val

            if root.left is not None:
                _level(root.left, level+1)
            if root.right is not None:
                _level(root.right, level+1)
        d = {}
        _level(root, 0)
        return max(d.keys())+1 if len(d) != 0 else 0


def printTree(x):
    if x is not None:
        print x.val
    if x.left is not None:
        printTree(x.left)
    if x.right is not None:
        printTree(x.right)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    # printTree(root)
    # root = None

    solution = Solution()
    print solution.maxDepth(root)


if __name__ == '__main__':
    main()