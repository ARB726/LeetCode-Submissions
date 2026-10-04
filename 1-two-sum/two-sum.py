class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}


        for i,j in enumerate(nums):

            total = target - j

            if total in hashMap:
                return [hashMap[total] , i]

            hashMap[j] = i

        return []

