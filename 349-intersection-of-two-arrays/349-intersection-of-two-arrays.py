"""
foreach element e in array A
    insert e into hash table H

foreach element e in array B
    if H contains e
        print e

This algorithm is O(N) in time and O(N) in space.

To avoid the extra space, you can use the sorting based approach.

http://stackoverflow.com/questions/13270491/best-way-to-find-an-intersection-between-two-arrays
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        rtn_list = []

        for n in nums1:
            hash_table[n] = True

        for n in nums2:
            if (n in hash_table) and (n not in rtn_list):
                rtn_list += [n]

        return rtn_list


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print solution.intersection(nums1, nums2)


if __name__ == '__main__':
    main()