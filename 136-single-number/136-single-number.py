class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = []
        for key, val in d.iteritems():
            if 1 == val:
                return key

        return -1 # failed to find single number



def main():
    nums = [1, 1, 2]

    solution = Solution()
    print solution.singleNumber(nums)


if __name__ == '__main__':
    main()