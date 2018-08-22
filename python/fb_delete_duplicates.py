# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        ptr = A
        while ptr!=None and ptr.next!=None:
            #print("p:%s n:%s v:%s" % (ptr==None, ptr.next==None, ptr.val))            
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return A