class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        l = list(s)
        sum = 0
        for digit in l:
            sum += int(digit)

        if len(list(str(sum))) == 1:
            return sum
        else:
            return self.addDigits(sum)


def main():
    num = 38

    solution = Solution()
    print solution.addDigits(num)


if __name__ == '__main__':
    main()