class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left , right , count , hashMap = 0 , 0 , 0 , {}

        while right < len(s):

            hashMap[s[right]] = hashMap.get(s[right] , 0) + 1

            while right - left + 1 > 3:

                hashMap[s[left]] -=1

                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]

                left +=1

            
            if right - left + 1 == 3 and len(hashMap) == 3:
                count +=1
            right +=1
        return count