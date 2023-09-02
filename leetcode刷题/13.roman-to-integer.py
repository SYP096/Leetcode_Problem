class Solution(object):
    def romanToInt(self, s):
        num = 0
        i = 0
        a = len(s)
        while a > 0:
            if i != len(s)-1:
                d = s[i] + s[i+1]
                if d in judge:
                    num += roman[s[i+1]] - roman[s[i]]
                    a -= 2
                    i += 2
                else:
                    num += roman[s[i]]
                    a -= 1
                    i += 1
            elif i == len(s) - 1:
                num += roman[s[i]]
                break

        return num


judge = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
print(Solution.romanToInt('', "MCMXCIV"))
