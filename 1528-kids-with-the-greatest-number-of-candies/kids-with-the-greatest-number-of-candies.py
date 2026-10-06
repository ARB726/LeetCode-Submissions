class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies