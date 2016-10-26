class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums[:])
        if len(n) < 3:
            return max(n)
        else:
            for i in xrange(2):
                n.remove(max(n))
            return max(n)

def main():
    nums = [3,2,1]

    solution = Solution()
    print solution.thirdMax(nums)


if __name__ == '__main__':
    main()