# solution reference:
#

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))

def main():
    num1 = "5"
    num2 = "6"

    solution = Solution()
    print solution.addStrings(num1, num2)


if __name__ == '__main__':
    main()