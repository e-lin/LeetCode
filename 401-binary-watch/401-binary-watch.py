# solution reference:
# http://bookshadow.com/weblog/2016/09/18/leetcode-binary-watch/

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for h in xrange(12):
            for m in xrange(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    ans.append("%d:%02d" % (h, m))
        return ans


def main():
    n = 5

    solution = Solution()
    print solution.readBinaryWatch(n)


if __name__ == '__main__':
    main()