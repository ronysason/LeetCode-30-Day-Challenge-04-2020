# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
class Solution:
    def singleNumber(self, nums) -> int:
        single_num = 0
        for x in nums:
            single_num = single_num ^ x

        return single_num


test01 = [2, 2, 1]
test02 = [4, 1, 2, 1, 2]
test03 = [2, 3, 5, 2, 3]
test04 = [500, 4334, 55553467, 500, 4334]


print(Solution().singleNumber(test04))
# print(Solution.singleNumber(test04))
# print(single_number(test02))
