class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 1
        if 1 == n:
            return 0
        else:
            if 0 == n%2:
                c += self.integerReplacement(n/2)
            else:
                c += min(self.integerReplacement(n-1), self.integerReplacement(n+1))
        return c



def main():
    n = 1001

    solution = Solution()
    print solution.integerReplacement(n)


if __name__ == '__main__':
    main()