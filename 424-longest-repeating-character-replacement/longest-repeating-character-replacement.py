class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , maxLength , hashMap , maxFreq , right = 0 , 0 , {} , 0 , 0
 

        while right < len(s):
            hashMap[s[right]] = hashMap.get(s[right],0) + 1
            maxFreq = max(maxFreq , hashMap[s[right]])

            while (right - left + 1) - maxFreq > k:
                    hashMap[s[left]] -=1

                    if hashMap[s[left]] == 0:

                        del hashMap[s[left]]

                    left +=1

            maxLength = max(maxLength , right - left +1)

            right +=1

        return maxLength


