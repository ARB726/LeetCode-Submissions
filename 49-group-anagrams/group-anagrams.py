class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)

        for char in strs:

            hashMap[tuple(sorted(char))].append(char)
        return list(hashMap.values())


