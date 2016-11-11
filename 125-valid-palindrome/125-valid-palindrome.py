import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        regex = re.compile('[^0-9a-zA-Z]')
        s = regex.sub('', s)

        for i in xrange(len(s)/2):
            if s[i].lower() != s[len(s)-i-1].lower():
                print  s[i],  s[len(s)-i-1]
                return False
        return True


def main():
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print solution.isPalindrome(s)


if __name__ == '__main__':
    main()