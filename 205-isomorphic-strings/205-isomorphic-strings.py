class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if 0 == len(s) and 0 == len(t):
            return True

        d = {} # key is char in s, value is char in t
        for i in xrange(len(s)):
            d[s[i]] = t[i]

        s_dict = {} # for char in s and its position
        for i in xrange(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]].append(i)

        t_dict = {} # for char in t and its position
        for i in xrange(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = [i]
            else:
                t_dict[t[i]].append(i)

        for key, val in d.iteritems():
            if s_dict[key] != t_dict[val]:
                return False

        return True


def main():
    s = "egg"
    t = "add"
    solution = Solution()
    print solution.isIsomorphic(s, t)


if __name__ == '__main__':
    main()