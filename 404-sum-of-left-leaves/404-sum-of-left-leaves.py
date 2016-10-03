# solution reference:
# http://bookshadow.com/weblog/2016/09/25/leetcode-sum-of-left-leaves/

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
        if root is None:
            return 0

        # is leaf
        if root.left is not None and \
        root.left.left is None and \
        root.left.right is None \
        :
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # is not leaf
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


def main():
    x = TreeNode(3)
    x.left = TreeNode(9)
    x.right = TreeNode(20)
    x.right.right = TreeNode(7)
    x.right.right.left = TreeNode(28)
    x.right.right.right = TreeNode(13)
    x.right.right.left.left = TreeNode(1)

    solution = Solution()
    print solution.sumOfLeftLeaves(x)


if __name__ == '__main__':
    main()