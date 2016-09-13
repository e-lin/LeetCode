
#allow space, minus, and plus
numbers = [' ', '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        my_list = list(s)
        start = 0
        stop = len(s)

        for idx, value in enumerate(my_list):
            if value in numbers and value != ' ': # CANNOT USE ---> value is not ' '
                start = idx
                break

        for idx, value in enumerate(my_list):
            if value not in numbers:
                stop = idx
                break

        new_str = ''.join(my_list[start:stop])

        if ' ' in new_str:  # for case "123  456", having space in the middle.
            new_str = new_str.split(' ')[0]

        try:
            integer = int(new_str)
        except ValueError:
            integer = 0

        if integer > INT_MAX:
            return INT_MAX
        elif integer < INT_MIN:
            return INT_MIN
        else:
            return integer


def main():
    # s = ""    # expected: 0
    # s = "+"   # expected: 0
    # s = "  -0012a42" # expected: -12
    # s = "+1" # expected: 1
    # s = "2147483648" # expected: 2147483647
    # s = "123  456" # expected: 123
    # s = "   +0 123" # expected: 0
    # s = "    010"  # expected: 10
    s = "    010" # expected: 10

    solution = Solution()
    print solution.myAtoi(s)

if __name__ == '__main__':
    main()