# Solution Reference:
# https://discuss.leetcode.com/topic/42931/sharing-very-simple-python-recursive-solution/2

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def _level(root, level):
            if root is None:
                return
            else:
                # print "level = " + str(level)
                # print root.val
                d[level] = d.get(level, []) + [root.val]

            if root.left is not None:
                _level(root.left, level+1)
            if root.right is not None:
                _level(root.right, level+1)

        d = {}
        _level(root, 0)
        return d.values()


def printTree(x):
    if x is not None:
        print x.val
    if x.left is not None:
        printTree(x.left)
    if x.right is not None:
        printTree(x.right)


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # printTree(root)

    solution = Solution()
    print solution.levelOrder(root)


if __name__ == '__main__':
    main()