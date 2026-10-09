class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxSum = 0

        for i in range(len(accounts)):

            
            totalSum = sum(accounts[i])

            maxSum = max (totalSum , maxSum)

        return maxSum