
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if 0 == len(nums):
            return 0

        curr = nums[0]
        end = 0
        for i in range(len(nums)):
            if val != nums[i]:
                curr = nums[i]
                nums[end] = nums[i]
                end += 1

        return end


def main():
    # nums = [3,2,3,2,3]
    # nums = [1]
    nums = []
    val = 0

    solution = Solution()
    print solution.removeElement(nums, val)


if __name__ == '__main__':
    main()