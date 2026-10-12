class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list) # to store elements that are anagrams into a list

        for char in strs:

            count = [0] * 26 # bc there are 26 characters from a-z

            for c in char:

                count[ord(c) - ord('a')] +=1

            
            hashMap[tuple(count)].append(char)

        return list(hashMap.values())
         