class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 == len(nums):
            return 0

        max_n = max(nums)
        # print max_n

        expected_sum_all = ((1 + max_n) * max_n) / 2
        actual_sum_all = sum(nums)

        if 0 == (expected_sum_all - actual_sum_all):
            if max_n == len(nums):
                return 0
            else:
                return len(nums)
        else:
            return expected_sum_all - actual_sum_all


def main():
    nums = [0, 1, 2, 3]

    solution = Solution()
    print solution.missingNumber(nums)


if __name__ == '__main__':
    main()