# As an array
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    if stack:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_stack(stack)
print(stack)

# As a Linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    rest = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return rest

# As a doubly linked-list
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None or head.next is None:
        if head:
            head.prev = None
        return head
    rest = reverse_doubly_linked_list(head.next)
    head.next.next = head
    head.prev = head.next
    head.next = None
    return rest


