class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashMap = {}

        for num in range(len(nums)):

            hashMap[nums[num]] = hashMap.get(nums[num],0) + 1

        for i , j in hashMap.items():

            if j > len(nums) / 2:
                return i