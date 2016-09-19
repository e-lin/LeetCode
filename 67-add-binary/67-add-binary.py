# solution reference:
# http://stackoverflow.com/questions/21420447/need-help-in-adding-binary-numbers-in-python

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binary = bin(int(a,2) + int(b,2))
        return str(binary[2:])

def main():
    a = "11"
    b = "1"

    solution = Solution()
    print solution.addBinary(a, b)


if __name__ == '__main__':
    main()