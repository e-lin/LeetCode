# solution reference:
# https://segmentfault.com/a/1190000003768716

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        end = 0

        for i in range(len(nums)):
            if 0 != nums[i]:
                nums[end] = nums[i]
                end += 1


        for i in range(end, length):
            nums[i] = 0

        print nums


def main():
    nums = [0,1,0,5,3,12]
    solution = Solution()
    solution.moveZeroes(nums)


if __name__ == '__main__':
    main()