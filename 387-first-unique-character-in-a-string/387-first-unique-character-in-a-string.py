class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        d = {}
        for i in xrange(len(s)):
            if s[i] not in d:
                d[s[i]] = (i, False) # record position i and repeat: Fasle
            else:
                d[s[i]] = (i, True)


        np_d = {k:v for k, v in d.items() if v[1] == False}

        if len(np_d) == 0:
            return -1
        else:
            t = min(np_d.values())
            return t[0]



def main():
    s = "loveleetcode"
    solution = Solution()
    print solution.firstUniqChar(s)


if __name__ == '__main__':
    main()