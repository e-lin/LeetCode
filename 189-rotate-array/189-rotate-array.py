class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - k
        nums[:] = nums[r:] + nums[:r]
        # MUST use "nums[:]"(call-by-value), NOT "nums"(call-by-reference)
        # http://www.python-course.eu/passing_arguments.php


def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print nums


if __name__ == '__main__':
    main()