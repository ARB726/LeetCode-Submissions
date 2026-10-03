class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        stack = []
        hashMap = {}

        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                a = stack.pop()
                hashMap[a] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):

            if nums1[i] in hashMap:
                ans.append(hashMap[nums1[i]])

            else: ans.append(-1)

        return ans