def check_snowfall_exceeds_half(n, cumulative):
    # Convert cumulative to daily snowfall
    daily = [cumulative[0]] + [cumulative[i] - cumulative[i - 1] for i in range(1, n)]
    total = cumulative[-1]
    half_total = total / 2

    # Check 3-day sliding window
    for i in range(n - 2):
        window_sum = daily[i] + daily[i + 1] + daily[i + 2]
        if window_sum > half_total:
            return "YES"
    return "NO"

def main():
    with open("snowfall_input1.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    cumulative = list(map(int, lines[1].split()))
    result = check_snowfall_exceeds_half(n, cumulative)
    print(f"{lines[1]} solution: {result}")

if __name__ == "__main__":
    main()
