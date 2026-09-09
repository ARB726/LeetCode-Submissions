class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 , hashMap2 = {} , {}
        for char in s:
            hashMap1[char] = hashMap1.get(char , 0) + 1
        
        for char in t:
            hashMap2[char] = hashMap2.get(char , 0) + 1

        return hashMap1 == hashMap2