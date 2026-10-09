class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        stack = []

        intervals.sort()

        for i in range(len(intervals)):


            if stack and intervals[i][0] <= stack[-1][1]:
                newVariable = stack[-1][0]
                newVariable = [stack[-1][0] , max(intervals[i][1],stack[-1][1])]

                stack.pop()
                stack.append(newVariable)
            else:
                stack.append(intervals[i])

        return stack