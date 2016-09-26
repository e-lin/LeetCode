class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pos = []
        char = []
        new_s = list(s)

        for i in xrange(len(s)):
            if s[i] in vowels:
                pos.append(i)
                char.append(s[i])
        # print pos
        # print char

        # reverse vowels
        for i in xrange(len(char)):
            new_pos = pos[len(pos)-1-i]
            new_s[new_pos] = char[i]
        # print new_s

        return ''.join(x for x in new_s)


def main():
    s = "leetcode"

    solution = Solution()
    print solution.reverseVowels(s)


if __name__ == '__main__':
    main()