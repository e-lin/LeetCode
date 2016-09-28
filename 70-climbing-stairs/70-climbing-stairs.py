# solution reference:
# https://segmentfault.com/a/1190000003707400
# https://segmentfault.com/a/1190000005146183

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        d[0] = 1
        d[1] = 1

        for i in xrange(2, n+1):
            d[i] = d[i-1] + d[i-2]

        return d[n]


def main():
    n = 35
    solution = Solution()
    print solution.climbStairs(n)


if __name__ == '__main__':
    main()