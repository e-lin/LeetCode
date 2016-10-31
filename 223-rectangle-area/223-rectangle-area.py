# solution reference:
# https://segmentfault.com/a/1190000003706797

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if C < E or D < F or G < A or H < B:
            cover = 0
        else:
            x1 = max(A, E)
            y1 = max(E, F)
            x2 = min(C, G)
            y2 = min(D, H)
            d1 = x2 - x1
            d2 = y2 - y1
            cover = d1 * d2

        return (C-A)*(D-B) + (G-E)*(H-F) - cover



def main():
    A = -2
    B = -2
    C = 2
    D = 2
    E = 8
    F = 4
    G = 13
    H = 6

    solution = Solution()
    print solution.computeArea(A, B, C, D, E, F, G, H)


if __name__ == '__main__':
    main()