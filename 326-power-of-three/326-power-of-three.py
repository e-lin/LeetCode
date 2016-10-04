# solution reference:
# http://bookshadow.com/weblog/2016/01/08/leetcode-power-three/

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0 or n % 3 > 0:
            return False
        return self.isPowerOfThree(n / 3)



def main():
    n = 27
    solution = Solution()
    print solution.isPowerOfThree(n)


if __name__ == '__main__':
    main()