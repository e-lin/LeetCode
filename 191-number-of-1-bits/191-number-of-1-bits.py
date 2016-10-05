class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        count = 0

        for i in s:
            if i == '1':
                count += 1

        return count


def main():
    nums = 11

    solution = Solution()
    print solution.hammingWeight(nums)


if __name__ == '__main__':
    main()