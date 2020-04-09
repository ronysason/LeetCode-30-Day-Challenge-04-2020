# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

class Solution:
    def countElements(self, arr) -> int:
        if arr == []:
            return 0

        count = 0
        elements = {}
        for x in arr:
            elements[x] = 1

        for x in arr:
            if x+1 in elements.keys():
                count += 1

        return count