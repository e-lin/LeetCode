class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]

        fill_zeros = 32 - len(s)
        if fill_zeros > 0:
            s = "0"*fill_zeros + s

        return int(s[::-1], 2) # convert bin to int


def main():
    n = 1

    solution = Solution()
    print solution.reverseBits(n)


if __name__ == '__main__':
    main()