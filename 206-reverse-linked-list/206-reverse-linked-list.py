# Solution Reference:
# http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html#reverse

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
        if head is None:
            return None
        if head.next is None:
            return head

        previous = None
        current = head
        preceding = head.next

        while preceding:
            current.next = previous
            previous = current
            current = preceding
            preceding = preceding.next

        current.next = previous #inverse the last node
        head = current
        return head


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