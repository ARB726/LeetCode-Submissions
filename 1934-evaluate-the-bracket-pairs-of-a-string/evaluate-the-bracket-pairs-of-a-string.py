class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hashMap = {}
        left = 0
        result = []
        for i , j in knowledge:

            hashMap[i] = j

        while left < len(s):

            if s[left] == '(':

                j = s.index(')',left)

                key = s[left+1:j]

                result.append(hashMap.get(key,'?'))

                left = j + 1

            else:
                result.append(s[left])

                left +=1

        return "".join(result)
        


