class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        smallnums = nums1[:] if len(nums1) < len(nums2) else nums2[:]
        bignums = nums1[:] if len(nums1) >= len(nums2) else nums2[:]
        l = []
        for i in smallnums:
            if i in bignums:
                l.append(i)
                bignums.remove(i)
        return l


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print solution.intersect(nums1, nums2)


if __name__ == '__main__':
    main()