
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = []
        for i in xrange(num+1):
            s = bin(i)[2:]
            count = 0

            for i in s:
                if i == '1':
                    count += 1
            l.append(count)
        return l


def main():
    n = 2
    solution = Solution()
    print solution.countBits(n)


if __name__ == '__main__':
    main()