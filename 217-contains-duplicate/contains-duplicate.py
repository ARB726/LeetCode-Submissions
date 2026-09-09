class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i , j in count.items():
            if j > 1:
                return True
        return False