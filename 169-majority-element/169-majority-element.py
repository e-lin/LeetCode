class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return max(d, key=lambda key: d[key])


def main():
    nums = [3,2,3]
    solution = Solution()
    print solution.majorityElement(nums)


if __name__ == '__main__':
    main()