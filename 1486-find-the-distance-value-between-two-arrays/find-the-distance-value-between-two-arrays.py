class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        count = 0
        j = 0
        for i in range(len(arr1)):

            while j < len(arr2) and arr2[j] < arr1[i] - d:

                j +=1

            if j == len(arr2) or arr2[j] > arr1[i] + d:
                count +=1

        return count
