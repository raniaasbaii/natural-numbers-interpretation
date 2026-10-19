
def get_splits(num):

    splits = []
    
    if 20 <= num <= 99 and num % 10 != 0:
        splits.append(str((num // 10) * 10) + str(num % 10))

    if 100 <= num <= 999 and num % 100 != 0:
        hundreds = (num // 100) * 100
        remainder = num % 100
        splits.append(str(hundreds) + str(remainder))
        if remainder >= 20 and remainder % 10 != 0:
            splits.append(
                str(hundreds) + str((remainder // 10) * 10) + str(remainder % 10)
            )

    return splits


def is_valid_greek_phone(s):
    if len(s) == 10:
        return s.startswith("2") or s.startswith("69")
    if len(s) == 14:
        return s.startswith("00302") or s.startswith("003069")
    return False


def find_all_interpretations(numbers):
    results = set()

    def backtrack(idx, current):
        if idx == len(numbers):
            results.add(current)
            return

        num = numbers[idx]

        backtrack(idx + 1, current + str(num))

        for s in get_splits(num):
            backtrack(idx + 1, current + s)

        if idx + 1 < len(numbers):
            nxt = numbers[idx + 1]
            if num % 10 == 0 and 20 <= num <= 90 and 1 <= nxt <= 9:
                backtrack(idx + 2, current + str(num + nxt))
            if num % 100 == 0 and 100 <= num <= 900 and 1 <= nxt <= 99:
                backtrack(idx + 2, current + str(num + nxt))

        if idx + 2 < len(numbers):
            a, b, c = num, numbers[idx + 1], numbers[idx + 2]
            if (
                a % 100 == 0
                and 100 <= a <= 900
                and b % 10 == 0
                and 20 <= b <= 90
                and 1 <= c <= 9
            ):
                backtrack(idx + 3, current + str(a + b + c))

    backtrack(0, "")
    return sorted(results)


def main():
    print("Natural Numbers Interpretation \n :")
    print("Enter numbers separated by spaces, or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("Input: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        try:
            numbers = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. please enter numbers separated by spaces.\n")
            continue

        interpretations = find_all_interpretations(numbers)

        print(f"\n{'#':<5} {'Output':<25} {'Phone number'}")
        print("-" * 50)
        for i, interp in enumerate(interpretations, 1):
            status = "VALID" if is_valid_greek_phone(interp) else "INVALID"
            print(f"{i:<5} {interp:<25} {status}")
        print()


if __name__ == "__main__":
    main()
