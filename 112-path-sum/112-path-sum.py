# solution reference:
# https://segmentfault.com/a/1190000003554851
# https://github.com/wizcabbit/leetcode.python/blob/master/112.Path.Sum.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, num):
        """
        :type root: TreeNode
        :type num: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            if num == root.val:
                return True

        return self.hasPathSum(root.left, num - root.val) \
            or self.hasPathSum(root.right, num - root.val)



def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    n = 22
    solution = Solution()
    print solution.hasPathSum(root, n)


if __name__ == '__main__':
    main()