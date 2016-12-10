# solution reference:
# http://cpmarkchang.logdown.com/posts/222651-minimum-edit-distance

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m

        # D(m, n) is the minimum edit distance for word1, word2
        # i, j is the substring of word1 with len i; and the substring of word2 with len j.
        D = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            D[i][0] = i
        for j in range(n+1):
            D[0][j] = j
        # for i in range(0,m+1):
        #     print D[i]
        # print "------------"
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1])
                else:
                    D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+1)

        # for i in range(0,m+1):
        #     print D[i]
        return D[m][n]


def main():
    # expected: 2
    word1 = "AGCCT"
    word2 = "ATCT"

    # expected: 0
    word1 = ""
    word2 = ""

    # expected: 3
    word1 = "b"
    word2 = "aaa"

    solution = Solution()
    print solution.minDistance(word1, word2)


if __name__ == '__main__':
    main()