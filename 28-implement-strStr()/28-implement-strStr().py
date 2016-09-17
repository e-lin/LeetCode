# solution reference:
# https://segmentfault.com/a/1190000003707284

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start = 0

        while (start <= len(haystack)-len(needle)):
            i1 = start
            i2 = 0
            while i2 < len(needle) and haystack[i1] == needle[i2]:
                i1 += 1
                i2 += 1
            if i2 == len(needle):
                return start

            start += 1

        return -1



def main():
    # haystack = "12345"
    # needle = "45"

    # haystack = ""
    # needle = "" # expected: 0

    haystack = "mississippi"
    needle ="issip" # expected: 4

    solution = Solution()
    print solution.strStr(haystack, needle)


if __name__ == '__main__':
    main()