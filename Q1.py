user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")

if nums:
    print(f"Largest: {max(nums)}")
    print(f"Smallest: {min(nums)}")

unique_nums = list(set(nums))
print(f"List after removing duplicates: {unique_nums}")