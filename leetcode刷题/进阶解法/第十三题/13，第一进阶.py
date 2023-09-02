'''leetcode 第13题的拓展, 这个解的很棒, 多学习'''
# s = 'MCMXCIV'
# for i, n in enumerate(s):    # enumerate() 枚举
#     print(i, n)
# print(list(enumerate(s)))
# print(max([1, 2, 3, 4, 5, 6]))

# An highlighted block


class Solution:
    def romanToInt_2(self, s):
        '''
  只能说秀   最主要看映射的设计
        '''
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        res_list = []
        for i, n in enumerate(s):
            # 每次都与上一个字母拼接
            s_lm = s[max(i - 1, 0):i + 1]
# 如果存在这个双字母，就用这个双字母，如果没有，就用n这个字母
            s_num = d.get(s_lm, d[n])

            res_list.append(s_num)

        return sum(res_list)


# return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
print(Solution.romanToInt_2('', 'MCMXCIV'))
