class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        result = []
        for i in range(k):
            frequent = max (count , key = count.get)
            result.append(frequent)
            del count[frequent]
            # print(result)
        return result


"""
SYNTAX:
most_common_item = max(c, key=c.get)

"""