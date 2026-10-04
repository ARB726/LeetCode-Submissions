class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = 0
        for i in range(len(nums)):
            nums[i] += prefix

            prefix = nums[i]

        return nums