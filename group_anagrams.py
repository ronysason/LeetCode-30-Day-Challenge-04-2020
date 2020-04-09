from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        temp = defaultdict(list)
        for ele in strs:
            temp[str(sorted(ele))].append(ele)
        return str(list(temp.values()))


test01 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(test01))