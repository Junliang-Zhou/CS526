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


