
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(" ")
        l = s.split(" ")
        last = l[(len(l)-1)]
        return len(last)



def main():
    s = "Hello "

    solution = Solution()
    print solution.lengthOfLastWord(s)


if __name__ == '__main__':
    main()