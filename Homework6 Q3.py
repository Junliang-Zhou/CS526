def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')

    n = int(lines[0])
    pref_lines = lines[1:]

    women_lines = pref_lines[:n]
    men_lines = pref_lines[n:2*n]

    women_prefs = {}
    men_prefs = {}

    for line in women_lines:
        parts = line.split()
        name, prefs = parts[0], parts[1:]
        women_prefs[name] = prefs

    for line in men_lines:
        parts = line.split()
        name, prefs = parts[0], parts[1:]
        men_prefs[name] = prefs

if __name__ == "__main__":
    men_prefs, women_prefs = read_input("marriage_hundred.txt")



