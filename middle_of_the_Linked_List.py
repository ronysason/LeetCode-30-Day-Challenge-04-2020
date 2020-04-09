# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
# The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        middleNode = head
        pointer = head
        counter = 0

        while pointer.next is not None:
            pointer = pointer.next
            counter += 1
            if counter % 2 != 0:
                middleNode = middleNode.next

        return middleNode

def arr_to_linked_list(arr):
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for x in range(1, len(arr)):
        cur.next = ListNode(arr[x])
        cur = cur.next

    return head


test01 = arr_to_linked_list([1, 2, 3, 4, 5])
test02 = arr_to_linked_list([1,2,3,4,5,6])
print(Solution().middleNode(test02).val)




