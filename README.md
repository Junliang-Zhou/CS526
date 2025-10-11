#Q1
def palindrome(p): # This uses recursion to check whether a string is a palindrome.
    if len(p) <= 1: # If the string has length 0 or 1, it’s trivially a palindrome.
        return True
    if p[0] != p[-1]: #This compares the first and last characters, if they’re different, it is not a palindrome.
        return False
    return palindrome(p[1:-1]) # Strip outer characters and check the inner substring

count = 0
with open("C:\BU Python\input_file.txt", "r") as file: # Before inputing any text file, I need to move the file to C:\BU Python folder. Then I change the "input_file" here to the actual file name.
    for line in file:
        word = line.strip()  # removes newline and spaces
        result = palindrome(word)
        print(str(result).lower()) # print "true" or "false" in lowr case
        if result:
            count += 1
print(count)

#Q2
def collect_substrings(s, start, current, seen):
    if start >= len(s):  # Base case: stop if we've reached the end of the string
        return
    current += s[start] # Add the next character to the current substring
    if current not in seen: # If it's a new substring, print it and add to the set
        print(current)
        seen.add(current)
    collect_substrings(s, start + 1, current, seen) # move to the next character

def unique_substrings(s):
    seen = set()
    for i in range(len(s)): # Start recursion from every index
        collect_substrings(s, i, "", seen)
    print("Total unique substrings:", len(seen))
    return seen

unique_substrings("abcab")

#Q3
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack_array(stack):
    if stack:
        temp = stack.pop()
        reverse_stack_array(stack)
        insert_at_bottom(stack, temp)

#Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head  # Base case: last node becomes new head

    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
    
#Double Linked List
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(node):
    if node is None:
        return None
    node.prev, node.next = node.next, node.prev  # Swap next and prev
    
    if node.prev is None: # If the original next was None, this node is the new head
        return node
    return reverse_doubly_linked_list(node.prev)




