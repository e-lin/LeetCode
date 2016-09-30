# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if (node != None) and (node.next != None):
            node.val = node.next.val
            node.next = node.next.next


def printListNode(x):
    if x is not None:
        print x.val
        if x.next is not None:
            printListNode(x.next)

def main():
    x = ListNode(1)
    x.next = ListNode(2)
    x.next.next = ListNode(3)
    x.next.next.next = ListNode(4)
    # printListNode(x)

    solution = Solution()
    solution.deleteNode(x.next.next)
    printListNode(x)


if __name__ == '__main__':
    main()