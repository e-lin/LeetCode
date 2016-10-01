class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False

        return True


def main():
    ransomNote = "saa"
    magazine = "bas"
    solution = Solution()
    print solution.canConstruct(ransomNote, magazine)


if __name__ == '__main__':
    main()