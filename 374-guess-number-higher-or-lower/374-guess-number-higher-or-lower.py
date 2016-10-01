# solution reference:
# https://www.hrwhisper.me/leetcode-guess-number-higher-lower/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num, myNum):
    if num > myNum:
        return -1
    elif num < myNum:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n, myNum):
        """
        :type n: int
        :rtype: int
        """
        L = 1
        R = n
        while L <= R:
            mid = L + (R-L)/2
            if guess(mid, myNum) == -1:
                R = mid - 1
            elif guess(mid, myNum) == 1:
                L = mid + 1
            else:
                return mid
        return L


def main():
    n = 100
    myNum = 46
    solution = Solution()
    print solution.guessNumber(n, myNum)


if __name__ == '__main__':
    main()