class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
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
              l.append(key)

        return l



def main():
    nums = [1,2,1,3,2,5]

    solution = Solution()
    print solution.singleNumber(nums)


if __name__ == '__main__':
    main()