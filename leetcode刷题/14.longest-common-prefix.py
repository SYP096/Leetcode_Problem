class Solution:
    # 这个答案是从Chatgpt找的
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        min_str = min(strs, key=len)  # 找到长度最小的字符串
        for i, char in enumerate(min_str):
            for other_str in strs:
                if other_str[i] != char:
                    return min_str[:i]
        return min_str


strs = ["flower", "flow", "flight"]
output = Solution.longestCommonPrefix('', strs)
print(output)
