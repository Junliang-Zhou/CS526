def max_items_selected(categories):
    left = 0
    max_len = 0
    basket = {}

    for right in range(len(categories)):
        cat = categories[right]
        basket[cat] = basket.get(cat, 0) + 1

        while len(basket) > 2:
            left_cat = categories[left]
            basket[left_cat] -= 1
            if basket[left_cat] == 0:
                del basket[left_cat]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

def main():
    with open("sc_input2.txt", "r") as f: # Change to sc_input2.txt to test another case
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    categories = [x.strip() for x in lines[1].split(',')]
    result = max_items_selected(categories)
    print(f"{result} items were selected")

if __name__ == "__main__":
    main()
