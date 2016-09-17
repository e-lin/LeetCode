
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for i in s:
            if i == ")":
                if 0 == len(stack) or stack.pop() != "(":
                    return False
            elif i == "]":
                if 0 == len(stack) or stack.pop() != "[":
                    return False
            elif i == "}":
                if 0 == len(stack) or stack.pop() != "{":
                    return False
            else:
                stack.append(i)

        if 0 == len(stack):
            return True
        else:
            return False



def main():
    # s = "[{()}[]]"
    # s = "()[]{}"
    s = "]"
    solution = Solution()
    print solution.isValid(s)


if __name__ == '__main__':
    main()