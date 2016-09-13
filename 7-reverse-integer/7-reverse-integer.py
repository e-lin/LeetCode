# solution reference:
# https://segmentfault.com/a/1190000002993867
# http://www.jiuzhang.com/solutions/reverse-integer/

# import math
# from numpy import isnan

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x > 0:
            inverse_str = s[::-1]
        elif x < 0:
            inverse_str = s[0] + s[1::][::-1]
        else:
            return 0

        integer = int(inverse_str)
        # if True == math.isnan(integer):
        if integer < -(1 << 31) or integer > (1 << 31) - 1:
            return 0
        else:
            return integer


def main():
    # x = 123   # expected: 321
    # x = -123  # expected: -321
    x = 1534236469  # expected: 0
    solution = Solution()
    print solution.reverse(x)

if __name__ == '__main__':
    main()