# solution reference:
# http://stackoverflow.com/questions/1804311/how-to-check-if-an-integer-is-a-power-of-3

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 0 == n:
            return False

        while n%2 == 0:
            n /= 2
        return 1 == n


def main():
    n = 27
    solution = Solution()
    print solution.isPowerOfTwo(n)


if __name__ == '__main__':
    main()