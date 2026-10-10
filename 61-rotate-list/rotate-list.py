# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if not head or not head.next: return head
        fast = head
        length = 1
        temp = head
        while fast.next:
            fast = fast.next

            length +=1

        if k % length == 0: return head
        else:
            k = k % length
        
        fast.next = head

        k = length - k -1
        while k != 0:

            temp = temp.next
            k -=1

        head = temp.next
        temp.next = None
        return head


        