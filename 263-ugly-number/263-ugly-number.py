# solution reference:
# https://segmentfault.com/a/1190000003921484

class Solution(object):
    #########  Time Limit Exceeded #########
    # def isPrime(self, num):
    #     for i in xrange(2, num):
    #         if 0 == num%i:
    #             return False
    #     return True

    # def findPrime(self, num):
    #     prime = []
    #     for i in xrange(2, num+1):
    #         if 0 == num%i and self.isPrime(i):
    #             print i
    #             prime.append(i)

    #     return prime

    # def isUgly(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if 0 >= num:
    #         return False
    #     if 1 == num:
    #         return True

    #     prime = self.findPrime(num)
    #     print prime
    #     ugly_prime = [2, 3, 5]

    #     for i in ugly_prime:
    #         if i in prime:
    #             prime.remove(i)

    #     if 0 == len(prime):
    #         return True
    #     else:
    #         return False
    #########  Time Limit Exceeded #########

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if 0 >= num:
            return False
        if 1 == num:
            return True

        pNum = num

        while 0 == pNum % 5:
            pNum /= 5

        while 0 == pNum % 3:
            pNum /= 3

        while 0 == pNum % 2:
            pNum /= 2

        if 1 == pNum:
            return True
        else:
            return False


def main():
    # n = 14
    # n = -2147483648
    n = 214797179

    solution = Solution()
    print solution.isUgly(n)


if __name__ == '__main__':
    main()