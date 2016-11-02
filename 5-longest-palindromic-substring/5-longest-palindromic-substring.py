# solution reference:
# https://segmentfault.com/a/1190000002991199
# https://github.com/ibab/leetcode-solutions/blob/master/005/main.go


class Solution(object):
    # ########## Time Limit Exceeded ###########
    #
    # Runtime: 312 ms with the case:
    # "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    #
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     matrix = [[True for y in range(len(s))] for x in range(len(s))]
    #     maxLength = 0
    #     maxStart = 0
    #
    #     # i: the length of palindrome string
    #     # j: the start position
    #     for i in range(len(s)):
    #         for j in range(len(s) - i):
    #             if 0 == i:
    #                 matrix[j][j+i] = True
    #             elif s[j] == s[j+i]:
    #                 matrix[j][j+i] = matrix[j+1][j+i-1]
    #             else:
    #                 matrix[j][j+i] = False
    #
    #             #notice: "i >= maxLength" should not be "i > maxLength", ortherwise you will fail at case "A"
    #             if (matrix[j][j+i] and i >= maxLength):
    #                 maxLength = i + 1
    #                 maxStart = j
    #     return s[maxStart:maxStart+maxLength]
    # ########## Time Limit Exceeded ###########


    # ########## Time Limit Exceeded ###########
    #
    # Runtime: 192 ms with the case:
    # "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    #
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     max_left = 0
    #     max_right = 0
    #
    #     for i in xrange(2*len(s)):
    #         left = i
    #         right = i
    #
    #         while left >= 0 and right < 2*len(s):
    #             if left%2 == 0 and s[left/2] != s[right/2]:
    #                 break
    #             left -= 1
    #             right +=1
    #
    #         left += 1
    #         right -= 1
    #
    #         real_left = (left + left%2)/2
    #         real_right = right/2 + 1
    #
    #         if (real_right - real_left) > (max_right - max_left):
    #             max_left = real_left
    #             max_right = real_right
    #
    #     return s[max_left:max_right]
    # ########## Time Limit Exceeded ###########

    max_left = 0
    max_right = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in xrange(len(s)):
            self.helper(s, i, 0) # for length of palindrome is odd
            self.helper(s, i ,1) # for length of palindrome is even
        return s[self.max_left+1:self.max_right]

    def helper(self, s, idx, offset):
        left = idx
        right = idx + offset
        while left >= 0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if (right - left) > (self.max_right - self.max_left):
            self.max_left = left
            self.max_right = right


def main():
    # s = "ABCCBA" #expected: "ABCCBA"
    # s = "A" #expected: "A"
    # s = "ABB" #expected: "BB"
    # s = "ccd" #expected: "cc
    # s = "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"
    # s = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    solution = Solution()
    print solution.longestPalindrome(s)


if __name__ == '__main__':
    main()