# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = list()
        curr = head
        while curr is not None:
            if curr.val not in l:
                l.append(curr.val)
                curr = curr.next
            else:
                curr = curr.next

        # make a listnode
        dummyHead = ListNode(0)
        p = dummyHead
        for val in l:
            node = ListNode(val)
            p.next = node
            p = p.next

        return dummyHead.next


def printNode(node):
    head = node
    while head is not None:
        print head.val
        head = head.next

def main():
    # head = ListNode(1)
    # head.next = ListNode(1)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(3)

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)

    solution = Solution()
    result = solution.deleteDuplicates(head)
    printNode(result)


if __name__ == '__main__':
    main()