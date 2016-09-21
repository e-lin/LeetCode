
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split(".")
        l2 = version2.split(".")

        if len(l1) >= len(l2):
            min = len(l2)
        else:
            min = len(l1)

        for i in range(min):
            if int(l1[i]) > int(l2[i]):
                return 1
            elif int(l1[i]) < int(l2[i]):
                return -1

        # compare the left elements in l1 or l2
        if len(l1) < len(l2):
            for i in range(min, len(l2)):
                if int(l2[i]) > 0:
                    return -1
            # all left elements in l2 are 0.
            return 0
        elif len(l1) > len(l2):
            for i in range(min, len(l1)):
                if int(l1[i]) > 0:
                    return 1
            # all left elements in l1 are 0.
            return 0
        else:
            return 0


def main():
    v1 ="1.0"
    v2 = "1"
    solution = Solution()
    print solution.compareVersion(v1, v2)


if __name__ == '__main__':
    main()