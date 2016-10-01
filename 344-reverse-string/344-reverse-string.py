class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


def main():
    s = "hello"
    solution = Solution()
    print solution.reverseString(s)


if __name__ == '__main__':
    main()