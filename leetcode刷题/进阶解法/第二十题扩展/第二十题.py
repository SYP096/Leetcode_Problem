class Solution:
    def isValid(self, s: str) -> bool:
        stack = []     # 建立一个空的栈
        for c in s:
            if c in '({[':        # 也可以是  if c=='(' or c == '[' or c == '{'
                stack.append(c)
            elif c in ')}]':
                if not stack:
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return not stack      # 也可以是 len(stack) == 0


strs = "()[]{}"
print(Solution.isValid('', strs))

'''
该解法与之前的解法基本思路相同   不同之处在于使用了if语句来进行括号匹配的比较。具体来说:

如果当前字符是左括号   则将其推入栈中。
如果当前字符是右括号   则从栈中弹出一个左括号并将其与当前右括号进行比较   如果不匹配   则返回False。
如果遍历结束后栈为空   则说明所有括号都匹配   返回True  否则返回False。
时间复杂度:O(n)

空间复杂度:O(n)
'''
