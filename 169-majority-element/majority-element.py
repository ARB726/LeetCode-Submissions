class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        Count = Counter(nums)

        for i , j in Count.items():

            if j > len(nums) / 2:
                return i