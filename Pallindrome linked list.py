"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""













# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        l = []
        n = head
        while(n):
            l.append(n.val)
            n = n.next
        

        if l[::-1] == l:
            return True

        return False
