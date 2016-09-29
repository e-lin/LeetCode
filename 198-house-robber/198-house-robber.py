# solution reference:
# https://segmentfault.com/a/1190000005138379
# https://segmentfault.com/a/1190000003811581

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if 0 == n:
            return 0

        dp = {}
        if 1 <= n:
            dp[0] = nums[0]

        if 1 < n:
            dp[1] = max(nums[0], nums[1])

        for i in xrange(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[n-1]


def main():
    # nums = [1,3,1,3,100]
    nums = [0]
    solution = Solution()
    print solution.rob(nums)


if __name__ == '__main__':
    main()