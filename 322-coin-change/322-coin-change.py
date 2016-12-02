# sokution reference:
# https://discuss.leetcode.com/topic/32529/two-short-pythons
# https://leetcode.com/articles/coin-change/


# (Dynamic programming - Bottom up)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        need = [0] + [amount+1]*amount
        for c in coins:
            for i in xrange(c, amount+1):
                need[i] = min(need[i], need[i-c]+1)
        print need
        return need[-1] if need[-1] <= amount else -1


# (Dynamic programming - Top down)
# Time Limit Exceeded with OJ
# Last executed input:
# [84,457,478,309,350,349,422,469,100,432,188]
# 6993
# Expected answer: 15

import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        count = [0]*amount
        return self._helper(coins, amount, count)

    def _helper(self, coins, remain, count):
        if remain < 0:
            return -1
        if remain == 0:
            return 0
        if count[remain-1] != 0:
            return count[remain-1]

        mini = sys.maxint
        for c in coins:
            res = self._helper(coins, remain-c, count)
            if res >= 0 and res < mini:
                mini = res + 1
        count[remain-1] = -1 if mini == sys.maxint else mini
        return count[remain-1]


def main():
    # expected return 3 (11 = 5 + 5 + 1)
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    print solution.coinChange(coins, amount)


if __name__ == '__main__':
    main()
