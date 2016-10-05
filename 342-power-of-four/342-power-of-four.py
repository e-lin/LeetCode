class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if 0 == num:
            return False

        while (num % 4) == 0:
            num /= 4
        return 1 == num



def main():
    n = 16
    solution = Solution()
    print solution.isPowerOfFour(n)


if __name__ == '__main__':
    main()