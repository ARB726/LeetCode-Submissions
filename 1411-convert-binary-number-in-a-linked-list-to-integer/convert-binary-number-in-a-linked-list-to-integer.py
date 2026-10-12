# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        num = head.val

        while head.next:
            num = num * 2 + head.next.val # this line doubles the value
            head = head.next
        return num




"""
Walkthrough :
1,0,1 nums = 1
"""