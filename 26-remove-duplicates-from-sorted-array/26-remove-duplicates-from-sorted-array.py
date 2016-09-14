# solution reference:
# https://segmentfault.com/a/1190000003752035

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 == len(nums):
            return 0

        duplicate = nums[0]
        end = 1
        for i in range(1, len(nums)):
            if nums[i] != duplicate:
                nums[end] = nums[i]
                duplicate = nums[i]
                end += 1

        return end

def main():
    # nums = [1,1,1,2,2,3]
    # nums = [1,1,1]
    nums = [1,1,1,1]
    solution = Solution()
    print solution.removeDuplicates(nums)



if __name__ == '__main__':
    main()