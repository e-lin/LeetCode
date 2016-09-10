# solution reference:
# https://segmentfault.com/a/1190000006697526

class Solution(object):
    def twoSum(self, nums, target):
        for idx, val in enumerate(nums):
            pair = target - val

            if pair in nums[idx+1 :]:
                print nums[idx+1 :]
                print pair

                jdx = nums[idx+1 :].index(pair) + idx+1
                break

        return idx,jdx


def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)

    print result


if __name__ == '__main__':
    main()