# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odds = self.connOdds(head)
        evens = self.connEvens(head)

        dummyHead = ListNode(0)
        dummyPtr = dummyHead
        p1 = odds
        p2 = evens

        while p1 is not None and p2 is not None:
            dummyPtr.next = ListNode(p2.val)
            dummyPtr = dummyPtr.next
            p2 = p2.next
            dummyPtr.next = ListNode(p1.val)
            dummyPtr = dummyPtr.next
            p1 = p1.next

        while p1 is not None:
            dummyPtr.next = ListNode(p1.val)
            dummyPtr = dummyPtr.next
            p1 = p1.next

        while p2 is not None:
            dummyPtr.next = ListNode(p2.val)
            dummyPtr = dummyPtr.next
            p2 = p2.next

        # printNode(dummyHead.next)
        return dummyHead.next

    def connOdds(self, head):
        if head is None:
            return None

        ptr = head
        dummyOdds = ListNode(0)
        dummyPtr = dummyOdds
        while ptr is not None:
            dummyPtr.next = ListNode(ptr.val)
            dummyPtr = dummyPtr.next

            if ptr.next is not None and ptr.next.next is not None:
                ptr = ptr.next.next
            else:
                ptr = None
        # printNode(dummyOdds.next)
        return dummyOdds.next

    def connEvens(self, head):
        if head is None or head.next is None:
            return None

        ptr = head.next
        dummyEvens = ListNode(0)
        dummyPtr = dummyEvens
        while ptr is not None:
            dummyPtr.next = ListNode(ptr.val)
            dummyPtr = dummyPtr.next

            if ptr.next is not None and ptr.next.next is not None:
                ptr = ptr.next.next
            else:
                ptr = None
        # printNode(dummyEvens.next)
        return dummyEvens.next


def printNode(node):
    ptr = node
    while ptr is not None:
        print ptr.val
        ptr = ptr.next

def main():
    node = ListNode(1)
    # node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)

    solution = Solution()
    result = solution.swapPairs(node)

    printNode(result)


if __name__ == '__main__':
    main()