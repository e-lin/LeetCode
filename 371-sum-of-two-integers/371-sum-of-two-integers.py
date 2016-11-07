# Solution Reference:
# http://bookshadow.com/weblog/2016/06/30/leetcode-sum-of-two-integers/
# https://www.hrwhisper.me/leetcode-sum-two-integers/

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


def main():
    # a, b = 1, 2
    # a, b = -12, -8 # expected: -20
    a, b = -1, 1

    solution = Solution()
    print solution.getSum(a, b)


if __name__ == '__main__':
    main()