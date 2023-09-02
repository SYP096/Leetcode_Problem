class Solution:
    def isValid(self, s: str) -> bool:
        def isValidRec(s: str, left: int, right: int) -> bool:
            if left == 0 and right == 0 and not s:
                return True
            if not s:
                return False
            if s[0] == '(':
                return isValidRec(s[1:], left+1, right)
            if s[0] == ')':
                if left == right:
                    return False
                return isValidRec(s[1:], left, right+1)
            if s[0] == '{':
                return isValidRec(s[1:], left, right)
            if s[0] == '}':
                if left == right:
                    return False
                return isValidRec(s[1:], left, right+1)
            if s[0] == '[':
                return isValidRec(s[1:], left, right)
            if s[0] == ']':
                if left == right:
                    return False
                return isValidRec(s[1:], left, right+1)
            return False
        return isValidRec(s, 0, 0)


'''
另一种解法是使用递归。具体来说  我们可以定义一个递归函数isValidRec
该函数接收一个字符串和左右括号的计数器作为参数
如果当前字符是左括号  则增加左括号计数器
如果当前字符是右括号  则增加右括号计数器
如果左右括号计数器相等且当前字符是右括号  则返回True  否则  继续遍历字符串。
如果遍历结束后左右括号计数器相等  则返回True  否则  返回False。'''
