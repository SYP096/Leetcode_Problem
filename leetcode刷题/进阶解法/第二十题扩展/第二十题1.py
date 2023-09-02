class Solution:
    # 这个的第89行一定要好好理解
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack


'''
还有一种解法是使用栈和哈希表。

我们可以使用一个栈来保存左括号, 对于每个右括号, 我们弹出栈顶的左括号进行匹配。
如果遍历完字符串后栈为空 则说明所有括号都匹配  否则 返回False。
我们可以使用哈希表来存储左右括号的对应关系 这样我们就可以很方便地进行匹配。v'''
