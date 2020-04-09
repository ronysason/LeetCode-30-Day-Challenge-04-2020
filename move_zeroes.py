# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.c
class Solution:
    def moveZeroes(self, nums) -> None:
        zeros = 0
        length = len(nums)

        for i in range(length):
            if nums[i] == 0:
                zeros += 1
            elif zeros > 0:
                nums[i - zeros] = nums[i]
            if i >= (length - zeros):
                nums[i] = 0
