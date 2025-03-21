# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for data in lst[1:]:
        current.next = Node(data)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def removeNthFromEnd(head: Node, n: int) -> Node:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

head_values = list(map(int, input().split()))
n = int(input())
head = create_linked_list(head_values)
new_head = removeNthFromEnd(head, n)
print_linked_list(new_head)
