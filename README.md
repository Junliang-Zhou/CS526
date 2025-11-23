# Homework6 Q1 Q2
Merge Sort: Recursively divide the array into halves, sort each half, then merge them
Quick Sort: Choose a pivot, partition into smaller/bigger, recursively sort partitions
Insertion Sort: Build the sorted array one item at a time by inserting into correct position
Radix Sort: Process digits from least significant to most significant.

Comparsion
Merge Sort: Time complexity is O(nlogn), use it for large datasets.
Quick Sort:	Time complexity average is O(nlogn), worst is O(n^2), use it for fast general sorting.
Insertion Sort:	Time complexity is O(n^2), use it for small datasets
Radix Sort:	Time complexity is O(𝑛𝑘) where k is number of digits, use it for sorting integers with bounded digit length

How to run the codes: I have my own example input files named as "HW6 Q1 Small Input.txt", "HW6 Q1 Medium Input.txt" and "HW6 Q1 Large Input.txt". I have uploaded them in the repository. Next, put code files and input files in the same folder. Before running the code, change the path of terminal to this folder.









# Homework5 Q1
My python file named as "Homework5 Q1.py". When running the code, we can type python3 "Homework5 Q1.py" in the terminal but the path of the terminal should include this python file.

Node ADT
Each node stores: A value, A left child, A right child
Created using: Node(value) This is the basic building block of the tree.

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
Uses in-order traversal: Left → Node → Right. This prints the values in sorted order.

Demo Code
Randomly generates an input set of size 5 to 50 with values between 1 and 1000. Builds the initial tree. Add a random value and prints the tree. Delete a random value and prints the tree.
Runs two FindNode tests: One for a value that exists. One for a value that does not exist

# Homework5 Q2
Using a dynamic programming array dp where:
dp[i] = number of valid vowel-only decodings for the first i symbols of the Morse string

Steps:
Initialize dp[0] = 1 (empty string has one valid decoding)
For each position i from 1 to n: Check if any vowel code ends at position i
If code[i-len(vowel):i] == vowel_code, then add dp[i-len(vowel)] to dp[i]
Final answer is dp[n] This counts all valid ways to split the Morse string using only vowel codes.

When running the code, it first asks the input file number. Enter 1 for vowel_input1.txt

# Homework5 Q3
Firstly, to build increasing subsequences: For each element in A, compute the longest increasing subsequence ending at that element and do the same for B.

Alternate and combine: Try combining elements from A and B such that they alternate and remain increasing.

We consider both patterns: Odd positions from A, even from B. Odd positions from B, even from A.

Track the best sequence: For each valid alternating pair, we build a candidate sequence and keep the longest one.

Return the best result: The final result is the longest alternating increasing sequence found.

How to run the code: Firstly we need to put this python file and all input files in the same folder. Then I use "cd" to change the path of terminal to that folder. I put longest_seq1.txt in the code as the first input file. When I want to run other files like longest_seq2, just change 1 to 2 in the code.

My code can run 1 and 2 correctly but wrong for the rest of input files. Sorry. 


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
