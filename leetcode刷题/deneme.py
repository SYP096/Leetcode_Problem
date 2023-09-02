class Solution:
    def longest(self, gress):
        if not gress:
            return ""
        zuiduan = min(gress, key=len)
        for x, y in enumerate(zuiduan):
            for o in gress:
                if o[x] != y:
                    return zuiduan[:x]
        return zuiduan


strs = ["flower", "flow", "flight"]
outout = Solution.longest('', strs)
print(outout)
