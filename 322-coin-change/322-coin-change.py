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




def main():
	# expected return 3 (11 = 5 + 5 + 1)
	coins = [1, 2, 5]
	amount = 11
	solution = Solution()
	print solution.coinChange(coins, amount)


if __name__ == '__main__':
	main()
