
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        MAX_INT = 0x7FFFFFFF # 32 bits integer max
        MIN_INT = 0x80000000 # 32 bits integer min
        MASK = 0xFFFFFFFF # mask to get last 32 bits

        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # if a is negative, get a's 32 bits complement positive first,
        # then get 32-bit positive's Python complement negative.
        return a if a <= MAX_INT else ~(a ^ MASK)


def main():
    # a, b = 1, 2
    # a, b = -12, -8 # expected: -20
    a, b = -1, 1

    solution = Solution()
    print solution.getSum(a, b)


if __name__ == '__main__':
    main()