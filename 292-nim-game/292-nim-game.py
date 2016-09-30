class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        left_stones = n % 4;

        if (0 == left_stones):
            return False;
        else:
            return True;
        end


def main():
    n = 5
    solution = Solution()
    print solution.canWinNim(n)


if __name__ == '__main__':
    main()