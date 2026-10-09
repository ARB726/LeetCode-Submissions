class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        stack = []

        for i in range(len(intervals)):

            if stack and intervals[i][0] <= stack[-1][1]:
                
                newVariable = [stack[-1][0],
                max(stack[-1][1],intervals[i][1])]
                a = stack.pop()
                stack.append(newVariable)
            else:
                stack.append(intervals[i])

        return stack