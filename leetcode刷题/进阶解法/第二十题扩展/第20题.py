class Solution:
    '''这个题你一定要好好看看, 这个题用到的逻辑真的太重要了'''
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


strs = "()[]{}"
print(Solution.isValid('', strs))
'''
解题思路：

遍历字符串中的每个字符。
如果字符是左括号   则将其推入栈中。
如果字符是右括号   则从栈中弹出一个左括号并将其与当前右括号进行比较   如果匹配   则继续遍历字符串   否则返回False。
如果遍历结束后栈为空   则说明所有括号都匹配   返回True   否则返回False。
时间复杂度:  O(n)

空间复杂度:  O(n)
'''
