# solution reference:
# https://segmentfault.com/a/1190000003849544

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if 1 == n:
            return "1"
        if 0 == n:
            return ""

        s = self.countAndSay(n-1)
        s_new = ""
        count = 1

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                s_new += str(count)
                s_new += s[i]
                count = 1

        s_new += str(count)
        s_new += s[len(s)-1]
        return s_new




def main():
    n = 2
    solution = Solution()
    print solution.countAndSay(n)


if __name__ == '__main__':
    main()