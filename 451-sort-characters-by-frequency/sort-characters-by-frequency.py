class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) # will map each character to count

        buckets = defaultdict(list)

        for i , j in count.items():

            buckets[j].append(i)

        result =""

        for i in range(len(s) , 0 , -1):

            for char in buckets[i]:

                result += char * i

        return result




















