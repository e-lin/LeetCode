# solution reference:
# http://bookshadow.com/weblog/2015/05/25/leetcode-contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

        # THIS CAUSE TIME LIMIT EXCEEDED
        # unique = list()
        # for n in nums:
        #     if n in unique:
        #         return True
        #     else:
        #         unique += [n]

        # return False



def main():
    nums = [1, 2, 2]

    solution = Solution()
    print solution.containsDuplicate(nums)


if __name__ == '__main__':
    main()