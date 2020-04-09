# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.

class Solution:
    def isHappy(self, n) -> bool:
        visited = {}
        return self.calc_digits(n, visited)

    def calc_digits(self, n, visited):
        if n == 1:
            return True
        if n in visited:
            return False

        visited[n] = 1
        num = str(n)
        digits = len(num)
        temp = 0

        for i in range(digits):
            temp += int(num[i]) ** 2

        return self.calc_digits(temp, visited)


print(Solution().isHappy(19))
print(Solution().isHappy(2))



