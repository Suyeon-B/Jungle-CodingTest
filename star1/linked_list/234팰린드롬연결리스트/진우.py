# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        
        while(head != None):
            list1.append(head.val)
            head = head.next
        
        list2 = list(reversed(list1))
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        else:
            return True