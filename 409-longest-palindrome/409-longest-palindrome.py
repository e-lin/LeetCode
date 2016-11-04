class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        l = d.values()

        length = 0
        hasOdd = False

        for i in l:
            if i%2 == 0:
                length += i
            else:
                hasOdd = True
                length += (i/2)*2

        if hasOdd:
            length += 1

        return length


def main():
    s = "abcccccddasssdd" # expected 13
    # s = "abcccccddassssssddabbwssdd" # expected 23
    # s = "aaabaaaa" # expected 7

    solution = Solution()
    print solution.longestPalindrome(s)


if __name__ == '__main__':
    main()