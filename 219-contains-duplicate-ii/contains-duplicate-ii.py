class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set ()

        for num in range(len(nums)):

            if nums[num] in hashSet:
                return True

            hashSet.add(nums[num])

            if len(hashSet) > k:

                hashSet.remove(nums[num - k])

        return False