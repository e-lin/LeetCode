class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        stmp = s
        number = 0
        for i in xrange(len(s)-1):
            ss = s[i]+s[i+1]
            if ss in roman:
                number += roman[ss]
                stmp = stmp.replace(ss, "") #remove ss

        for i in stmp:
            if i in roman:
                number += roman[i]

        return number


def main():
    s = "XIX"
    solution = Solution()
    print solution.romanToInt(s)

if __name__ == '__main__':
    main()