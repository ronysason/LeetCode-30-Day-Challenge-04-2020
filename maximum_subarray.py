# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums) -> int:

        cur_max = nums[0]
        best_max = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max+nums[i])
            best_max = max(best_max, cur_max)

        return best_max


test01 = [0, 0, 0]
print(Solution().maxSubArray(test01))

