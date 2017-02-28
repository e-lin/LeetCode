# solution reference:
# https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation/69
# https://discuss.leetcode.com/topic/22356/python-o-lg-m-n-recursive-solution

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

# O(log(min(m,n)))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1[:], nums2[:]
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        i = self._searchi(A, B, 0, m, 0, n)
        return A[i]

    def _searchi(self, A, B, lm, rm, ln, rn):
        for i in range(rm):
            # as we need to satisfy i + j == m - i + n - j + 1
            j = (rm + rn + 1) / 2 - i
            print i, j
            if (i == 0 or j == rn or A[i-i] <= B[j]) and \
                (j == 0 or i == rm or B[j-1] <= A[i]):
                # print "A[i-1], A[i] %s, %s" % (A[i-1], A[i])
                # print "B[j-1], B[j] %s, %s" % (B[j-1], B[j])
                print "here: i = %s" % i
                return i
            elif i > 0 and j < rn and A[i-1] > B[j]: pass
                # self._searchi(A, B, lm+1, rm, ln, rn)
            elif j > 0 and i < rm and B[j-1] > A[i]: pass
                # self._searchi(A, B, lm-1, rm, ln, rn)


def main():
    nums1 = [1,3]
    nums2 = [2,4]

    solution = Solution()
    print solution.findMedianSortedArrays(nums1, nums2)

if __name__ == '__main__':
    main()