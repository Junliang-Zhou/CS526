def palindrome(p):
    if len(p) <= 1:
        return True
    if p[0] != p[-1]:
        return False
    return palindrome(p[1:-1])

count = 0
with open("C:\BU Python\palendrome_0S.txt", "r") as file:
    for line in file:
        word = line.strip()
        result = palindrome(word)
        print(str(result).lower())
        if result:
            count += 1
print(count)

    


