# An highlighted block
class Solution:
    def romanToInt(self, s):

        num_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0
        # 需要找出  数字之间的规律    4  10  分别是  IV  IX   也就是说  他的第一位小于第二位
        # 但是类似正常的  82  LXXXII  都是第一位大于第二位  所以这就是规律
        for i in range(len(s)):
            if i < len(s)-1 and num_roman[s[i]] < num_roman[s[i+1]]:      # 防止过界
                ans -= num_roman[s[i]]    # 减去小的这一位，然后再加上大的后面的那位
            else:
                ans += num_roman[s[i]]

        return ans


print(Solution.romanToInt('', 'MCMXCIV'))
