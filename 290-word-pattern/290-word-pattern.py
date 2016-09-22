# solution reference:
#

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_lst = s.split(" ")
        if len(pattern) != len(s_lst):
            return False

        # key, value for pattern and string
        dic = {}
        for i in range(len(pattern)):
            dic[pattern[i]] = s_lst[i]
        print dic


        pattern_dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dic:
                pattern_dic[pattern[i]] = [i] # record the pattern and position
            else:
                pattern_dic[pattern[i]].append(i) # record the position

        s_dic = {}
        for i in range(len(s_lst)):
            if s_lst[i] not in s_dic:
                s_dic[s_lst[i]] = [i]
            else:
                s_dic[s_lst[i]].append(i)

        print pattern_dic
        print s_dic


        for key, value in dic.iteritems():
            if pattern_dic[key] != s_dic[value]:
                return False
        return True


def main():
    # pattern = "abba"
    # s = "dog cat cat dog"

    # pattern = "he"
    # s = "unit"

    pattern = "ab"
    s = "b c"

    solution = Solution()
    print solution.wordPattern(pattern, s)


if __name__ == '__main__':
    main()