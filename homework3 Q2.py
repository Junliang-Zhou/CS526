def collect(s, substrings):
    if not s:
        return
    for i in range(1, len(s) + 1):
        substrings.add(s[:i])
    collect(s[1:], substrings)

def unique_substrings(s):
    substrings = set()
    collect(s, substrings)
    for sub in substrings:
        print(sub)
    print("Total unique substrings:", len(substrings))

unique_substrings("abcab")
