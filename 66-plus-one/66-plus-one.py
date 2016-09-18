
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(str(d) for d in digits)
        num = int(s)
        num += 1

        s = str(num)
        l = []
        for i in s:
            l.append(int(i))
        return l



def main():
    digits = [1, 3, 5, 7]

    solution = Solution()
    print solution.plusOne(digits)


if __name__ == '__main__':
    main()