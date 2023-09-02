class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list1.extend(list2)
        list1.sort()
        return list1


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(Solution.mergeTwoLists('', list1=list1, list2=list2))
