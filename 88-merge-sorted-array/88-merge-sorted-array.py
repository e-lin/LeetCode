# solution reference:
# https://segmentfault.com/q/1010000006854432

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


def main():
    nums1 = [3, 1, 5, 7]
    nums2 = [2, 4, 6]
    m = 3
    n = 2
    solution = Solution()
    solution.merge(nums1, m, nums2, n)


if __name__ == '__main__':
    main()