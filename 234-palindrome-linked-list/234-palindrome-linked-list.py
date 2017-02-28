# Solution Reference:
# https://discuss.leetcode.com/topic/18293/11-lines-12-with-restore-o-n-time-o-1-space

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """




def main():
    # expected: True
    head = ListNode(-1)
    head.next = ListNode(-1)

    # expected: False
    head = ListNode(-1)
    head.next = ListNode(1)

    solution = Solution()
    print solution.isPalindrome(head)

if __name__ == '__main__':
    main()