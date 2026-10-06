class Solution:
    def canJump(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums)):

            if i > count:
                return False

            count = max(count, i + nums[i])

            if count >= len(nums)-1:
                return True
        return True