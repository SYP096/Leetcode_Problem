class Solution(object):
    def isValid(self, s):
        judge = []
        for i in s:
            if i in dic:
                if not judge or judge[-1] != dic[i]:      # judge=[], False,,,and return False...... or 两个都是True的时候才会执行
                    return False
                else:      # 只有judge不为空值， 以及judge的最后一个元素和字典对应元素一样时，才会执行这一行
                    judge.pop()
            else:
                judge.append(i)
        return not judge


dic = {')': '(', ']': '[', '}': '{'}
s = "(]"
print(Solution.isValid('', s))
