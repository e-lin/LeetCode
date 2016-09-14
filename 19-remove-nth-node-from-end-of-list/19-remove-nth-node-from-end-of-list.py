# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        length = self.countNodeLength(ptr)
        idx = length - n #position to remove

        if 0 == idx:
            return head.next

        for i in range(idx-1): #find the previous one
            ptr = ptr.next

        # print "ptr to delete: " + str(ptr.next.val)
        ptr.next = ptr.next.next
        return head


    def countNodeLength(self, node):
        ptr = node
        length = 0
        while ptr is not None:
            length += 1
            ptr = ptr.next

        return length


def printNode(node):
    ptr = node
    while ptr is not None:
        print ptr.val
        ptr = ptr.next

def main():
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    n = 1
    solution = Solution()
    result = solution.removeNthFromEnd(node, n)

    printNode(result)


if __name__ == '__main__':
    main()