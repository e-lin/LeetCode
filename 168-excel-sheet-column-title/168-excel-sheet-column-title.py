class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        title = ""
        A = ord('A') #65

        while n:
            title += chr((n - 1) % 26 + A)
            n = (n - 1) / 26
            self.convertToTitle(n)


        return title[::-1]


def main():
    n = 28
    solution = Solution()
    print solution.convertToTitle(n)


if __name__ == '__main__':
    main()