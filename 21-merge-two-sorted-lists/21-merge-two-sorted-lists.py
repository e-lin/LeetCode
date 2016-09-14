# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyPtr = dummyHead
        p1 = l1
        p2 = l2

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                dummyPtr.next = ListNode(p1.val)
                dummyPtr = dummyPtr.next
                p1 = p1.next
            else:
                dummyPtr.next = ListNode(p2.val)
                dummyPtr = dummyPtr.next
                p2 = p2.next

        while p1 is not None:
            dummyPtr.next = ListNode(p1.val)
            dummyPtr = dummyPtr.next
            p1 = p1.next

        while p2 is not None:
            dummyPtr.next = ListNode(p2.val)
            dummyPtr = dummyPtr.next
            p2 = p2.next

        return dummyHead.next


def printNode(node):
    ptr = node
    while ptr is not None:
        print ptr.val
        ptr = ptr.next

def main():
    l1 = ListNode(2)
    l1.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    printNode(result)


if __name__ == '__main__':
    main()