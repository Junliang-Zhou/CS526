# Homework5 Q1
My python file named as "Homework5 Q1.py". When running the code, we can type python3 "Homework5 Q1.py" in the terminal
Node ADT
Each node stores: A value, A left child, A right child
Created using: Node(value)
This is the basic building block of the tree.
BST ADT
The BST stores: A root node and methods to add, delete, find and print nodes.
AddNode
Inserts a value into the tree.
If the tree is empty, the value becomes the root.
Otherwise: If value < current node → go left; If value > current node → go right; If value == current node → do nothing. Using recursion to find the correct spot.
DeleteNode
Removes a node from the tree.
Three cases: No children → just remove the node; One child → replace node with its child; Two children → find the smallest value in the right subtree (inorder successor), replace the node’s value, then delete the successor. Using recursion to find and remove the node.
FindNode
Searches for a value in the tree.
Starts at the root and moves left or right depending on comparison. Returns True if found, False otherwise.
PrintTree()
Uses in-order traversal: Left → Node → Right
This prints the values in sorted order.
Demo Code
Randomly generates an input set of size 5 to 50 with values between 1 and 1000. Builds the initial tree.
Adds a random value and prints the tree. Deletes a random value and prints the tree.
Runs two FindNode tests: One for a value that exists. One for a value that does not exist






















# MID-TERM – 4 Problems

This repository contains solutions to 4 problems:  
**Snowfall**, **Pandemic**, **Shopping Cart**, and **Symbol Puzzle Game**.

---

## Files Included

- `mid-term Q1.py`
- `mid-term Q2.py`
- `mid-term Q3.py`
- `mid-term Q4.py`
- `Heart of Algorithm.docx`
- `Output Screenshots.docx`

##How to run codes

Each Python file is a solution of one problem. In all soultions, I put input1 file for each question as a sample. If you want to run other input files, you can just change 1 to other numbers.

python mid-term Q1.py
python mid-term Q2.py
python mid-term Q3.py
python mid-term Q4.py

---

## Homework 4
Q1
Preorder Traversal starting from the root then visit each child from left to right
Breadth-First Traversal. we visit nodes level by level from top to bottom, and within each level, from left to right.
For post, we visit all children from left to right then visit the parent node.
In in-order traversal, we visit the left subtree then the current node then the right subtree.
