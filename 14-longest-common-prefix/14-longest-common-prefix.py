class Solution(object):
    def compareCommon(self, strs, j, i, s1):
        while j < len(strs):
            if s1[i] != strs[j][i]:
                return ""
            else:
                j += 1
        return s1[i]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if 0 == len(strs):
            return ""
        if 1 == len(strs):
            return strs[0]

        # sorting list based on the length of the string
        strs.sort(lambda x,y: cmp(len(x), len(y)))

        s1 = strs[0] # the shortest one
        i = 0
        common = str()

        while i < len(s1):
            j = 1
            cmchar = self.compareCommon(strs, j, i, s1)
            if "" == cmchar:
                return common # do not compare anymore.
            else:
                common += cmchar

            # print "common = " + common
            i += 1

        return common


def main():
    # strs = ["a2543112", "a25431324", "a25"]
    # strs = ["a","b"] # expected: ""
    strs = ["aca","cba"] # expected: ""
    # strs = ["a"] # expected: "a"
    # strs = ["c","c"] # expected: "c"

    solution = Solution()
    print solution.longestCommonPrefix(strs)


if __name__ == '__main__':
    main()