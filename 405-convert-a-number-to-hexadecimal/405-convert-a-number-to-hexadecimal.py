class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = { 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f' }
        l = list(bin(num)[2:])
        l = l[::-1]
        l.extend('0' * (4*(len(l)/4+1) - len(l)))

        group = 0
        hex_result = ""
        temp = 0

        for i in xrange(len(l)):
            temp += (int(l[i]) * (2**group))

            if group == 3:  # start from 0 and every 4 is a group
                if temp < 10:
                    hex_result += str(temp)
                else:
                    hex_result += str(d[temp])
                temp = 0
                group = 0
            else:
                group += 1

        return hex_result[::-1]


def main():
    n = -1
    solution = Solution()
    print solution.toHex(n)


if __name__ == '__main__':
    main()