class Solution(object):
    def twoSum(self, nums=list[int], target=int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


a = Solution.twoSum('', nums=[2, 7, 11, 15], target=9)
print(a)
