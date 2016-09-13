
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 > x:
            return False

        if 0 == x:
            return True

        s = str(x)
        s.replace(" ","") #remove all spaces

        if s == s[::-1]:
            return True
        else:
            return False


def main():
    x = 12321

    solution = Solution()
    print solution.isPalindrome(x)

if __name__ == '__main__':
    main()