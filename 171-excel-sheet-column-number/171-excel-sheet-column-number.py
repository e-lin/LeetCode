class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if 0 == len(s):
            return 0

        s_lst = list(s[::-1])
        A = ord('A')
        num = ord(s_lst[0]) - A + 1

        for i in range(1, len(s_lst)):
            num += (ord(s_lst[i]) - A + 1) * pow(26, i)

        return num


def main():
    s = "AACD"
    solution = Solution()
    print solution.titleToNumber(s)


if __name__ == '__main__':
    main()