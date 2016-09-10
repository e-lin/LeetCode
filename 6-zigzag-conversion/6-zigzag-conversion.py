# solution reference:
# https://segmentfault.com/a/1190000005751185

class Solution(object):
    def convert(self, s, numRows):
        if (1 == numRows):
            return s

        str_builder = str()
        magicNum = 2*numRows - 2
        initDistance = magicNum

        for k in range(numRows):
            str_builder += self.fill(str(), k, initDistance, magicNum, s)
            initDistance -= 2
            # print "fill(" + str(k) + ") = "+ str_builder
        return str_builder


    def fill(self, strResult, startIdx, initDistance, magicNum, s):
        while startIdx < len(s):
            if 0 == initDistance:
                initDistance = magicNum
            strResult += s[startIdx]
            startIdx += initDistance
            initDistance = magicNum - initDistance

        return strResult


def main():
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)

    print result


if __name__ == '__main__':
    main()