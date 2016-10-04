# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        ptr = head

        while ptr is not None:
            lst.append(ptr.val)
            ptr = ptr.next

        # print lst
        lst = lst[::-1]

        rlst = ListNode(0) # dummy head
        rptr = rlst

        for i in lst:
            rptr.next = ListNode(i)
            rptr = rptr.next

        return rlst.next


def printListNode(head):
    while head is not None:
        print head.val
        head = head.next


def main():
    # ListNode = [2, 3, null, 4]
    head = ListNode(2)
    head.next = ListNode(3)
    head.next.next = ListNode(None)
    head.next.next.next = ListNode(4)

    solution = Solution()
    printListNode(solution.reverseList(head))


if __name__ == '__main__':
    main()