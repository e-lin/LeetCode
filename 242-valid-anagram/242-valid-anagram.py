# soultion reference:
# http://stackoverflow.com/questions/9623114/check-if-two-unordered-lists-are-equal

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_list = list(s)
        t_list = list(t)
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        return compare(s_list, t_list)

        # NOT FOR DUPLICATE CASE...ex: set([a, a]) equals to set([a])
        # return set(s_list) == set(t_list)

        # THIS WILL EXCEED EXECUTIOM TIME
        # if len(s) <= len(t):
        #     t_list = list(t)
        #     for i,ss in enumerate(s):
        #         if ss in t_list:
        #             t_list.remove(ss)
        #     if len(t_list) == 0:
        #         return True
        #     else:
        #         return False
        # else:
        #     s_list = list(s)
        #     for i, tt in enumerate(t):
        #         if tt in s_list:
        #             s_list.remove(tt)
        #     if len(s_list) == 0:
        #         return True
        #     else:
        #         return False



def main():
    s = "anagram"
    t = "nagaram"

    solution = Solution()
    print solution.isAnagram(s, t)


if __name__ == '__main__':
    main()