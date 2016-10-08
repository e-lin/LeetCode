class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if 0 == numRows:
            return []
        if 1 == numRows:
            return [[1]]

        result = [[1], [1,1]]

        for i in xrange(3, numRows+1):
            l = [0]*i
            l[0] = 1
            for j in xrange(1, i - 2 + 1):
                l[j] = result[i-2][j-1] + result[i-2][j]
            l[i-1] = 1
            result.append(l)

        return result

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = self.generate(rowIndex+1)
        return result[rowIndex]



def main():
    nums = 3
    solution = Solution()
    print solution.getRow(nums)


if __name__ == '__main__':
    main()