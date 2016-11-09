class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        for k in xrange(1, n):
            if n < (k+1)*(k+1+1)/2 and n >= k*(k+1)/2:
                return k


def main():
    n = 2146467960
    solution = Solution()
    print solution.arrangeCoins(n)


if __name__ == '__main__':
    main()