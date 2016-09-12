# solution reference:
# https://segmentfault.com/a/1190000002986101

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        add = 0
        carry = 0

        if l1 is None and l2 is None:
            return dummyHead

        while l1 is not None or l2 is not None:
            if l1 is None:
                a1 = 0
            else:
                a1 = l1.val

            if l2 is None:
                a2 = 0
            else:
                a2 = l2.val

            add = a1 + a2 + carry
            curr.next = ListNode(add%10)
            curr = curr.next
            carry = add/10

            if l1 is None:
                l1 = None
            else:
                l1 = l1.next

            if l2 is None:
                l2 = None
            else:
                l2 = l2.next

        # final check for carry
        if 1 == carry:
            curr.next = ListNode(1)

        return dummyHead.next


def printNode(node):
    ptr = node

    while ptr.next is not None:
        print ptr.val
        ptr = ptr.next
    print ptr.val # last one


def main():
    l1 = ListNode(2)
    l1_a = ListNode(4)
    l1_b = ListNode(3)
    l1.next = l1_a
    l1_a.next = l1_b
    # printNode(l1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # printNode(l2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    printNode(result)


if __name__ == '__main__':
    main()