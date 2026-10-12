class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)

        for char in strs:

            count = [0] * 26

            for c in char:

                count[ord(c)- ord('a')] +=1

            hashMap [tuple(count)].append(char)

        
        return list(hashMap.values())