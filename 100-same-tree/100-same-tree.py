# solution reference:
# https://discuss.leetcode.com/topic/46717/python-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False



def printTree(root):
    print root.val
    l = root.left
    r = root.right

    if l is not None:
        printTree(l)

    if r is not None:
        printTree(r)


def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    # printTree(t1)

    t2 = TreeNode(1)
    t2.left = TreeNode(None)
    t2.right = TreeNode(2)
    # printTree(t2)


    solution = Solution()
    print solution.isSameTree(t1, t2)


if __name__ == '__main__':
    main()