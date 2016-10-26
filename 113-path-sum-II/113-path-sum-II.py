# solution reference:
# https://segmentfault.com/a/1190000003554851

from copy import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    global paths
    paths = []
    def pathSum(self, root, num):
        """
        :type root: TreeNode
        :type num: int
        :rtype: List[List[int]]
        """
        routes = []
        self.traverseall(root)
        # print paths
        for path in paths:
            # print path
            if num == sum(path):
                routes.append(path)
        del paths[:]
        return routes


    def traverseall(self,node, path=None):
        # path = path or []
        if path is None:
            path = []

        if node is None:
            return

        path.append(node.val)

        if node.left is None and node.right is None: # is leaf
            # print path
            paths.append(path)
        else:
            if node.left is not None:
                self.traverseall(node.left, copy(path)) # MUST USE COPY
            if node.right is not None:
                self.traverseall(node.right, copy(path)) # MUST USE COPY



def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    n = 22

    solution = Solution()
    print solution.pathSum(root, n)

    root = TreeNode(1)
    root.left = TreeNode(2)
    n = 1

    # solution = Solution()
    print solution.pathSum(root, n)


if __name__ == '__main__':
    main()