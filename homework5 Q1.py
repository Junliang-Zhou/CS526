import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def AddNode(self, value):
        def _add(node):
            if node is None: return Node(value), True
            if value == node.value: return node, False
            if value < node.value:
                node.left, inserted = _add(node.left)
            else:
                node.right, inserted = _add(node.right)
            return node, inserted
        self.root, inserted = _add(self.root)
        return inserted

    def DeleteNode(self, value):
        def _delete(node):
            if node is None: return None, False
            if value < node.value:
                node.left, deleted = _delete(node.left)
                return node, deleted
            if value > node.value:
                node.right, deleted = _delete(node.right)
                return node, deleted
            if node.left is None: return node.right, True
            if node.right is None: return node.left, True
            succ = node.right
            while succ.left: succ = succ.left
            node.value = succ.value
            node.right, _ = _delete(node.right)
            return node, True
        self.root, deleted = _delete(self.root)
        return deleted

    def FindNode(self, value):
        node = self.root
        while node:
            if value == node.value: return True
            node = node.left if value < node.value else node.right
        return False

    def PrintTree(self):
        def _inorder(n):
            return _inorder(n.left) + [n.value] + _inorder(n.right) if n else []
        print("In-order:", _inorder(self.root))

# === DEMO ===
random.seed()  # or use random.seed(1234) for reproducible results
size = random.randint(5, 50)
input_set = random.sample(range(1, 1001), size)
print("Input set:", input_set)

bst = BST()
for v in input_set:
    bst.AddNode(v)

print("\nInitial tree:")
bst.PrintTree()

# AddNode
add_val = random.randint(1, 1000)
print(f"\nAddNode({add_val}):", bst.AddNode(add_val))
bst.PrintTree()

# DeleteNode
del_val = random.choice(input_set)
print(f"\nDeleteNode({del_val}):", bst.DeleteNode(del_val))
bst.PrintTree()

# FindNode (positive and negative)
pos_val = random.choice(input_set)
neg_val = next(v for v in range(1, 1001) if v not in input_set)
print(f"\nFindNode({pos_val}):", bst.FindNode(pos_val))  # should be True
print(f"FindNode({neg_val}):", bst.FindNode(neg_val))    # should be False

