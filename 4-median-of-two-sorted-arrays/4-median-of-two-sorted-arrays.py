# solution reference:
#

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1 + nums2
        a.sort()                    # time conplexity: n*log(n)
        if len(a)%2 == 1:
            return a[len(a)/2]
        else:
            b = a[len(a)/2 - 1]
            c = a[len(a)/2]
            return (b+c)/2.0

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


def main():
    nums1 = [1,3]
    nums2 = [2,4]

    solution = Solution()
    print solution.findMedianSortedArrays(nums1, nums2)

if __name__ == '__main__':
    main()