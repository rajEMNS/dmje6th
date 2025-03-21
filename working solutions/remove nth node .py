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
        print(current.data,end =" ")
        current = current.next
    print()
    
def remove_node(nums,k):
    fast = slow = head
    for i in range(k):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
    
n = int(input())
nums = list(map(int,input().split()))
k = int(input())
head = create_linked_list(nums)
new_node = remove_node(nums,k)
print_linked_list(new_node)
        