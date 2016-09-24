class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_lst = list(t)

        for i in s:
            if i in t_lst:
                t_lst.remove(i)

        if 1 == len(t_lst):
            return str(t_lst[0])
        else:
            return "-1" # failed to find the difference



def main():
    s = "abcd"
    t = "baadc"

    solution = Solution()
    print solution.findTheDifference(s, t)


if __name__ == '__main__':
    main()