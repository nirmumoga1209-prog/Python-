def collect_and_count_unique():
    nums = []
    while len(nums) < 10:
        try:
            val = int(input(f"Enter number {len(nums)+1}: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        nums.append(val)

    unique_nums = set(nums)
    print("Entered numbers:", nums)
    print("Unique numbers:", list(unique_nums))
    print("Count of unique numbers:", len(unique_nums))


if __name__ == "__main__":
    collect_and_count_unique()
