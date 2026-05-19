nums = [10, 5, 20, 8, 15]

print("Max value:", max(nums))
print("Min value:", min(nums))
print("Sum:", sum(nums))


nums.sort()
print("Ascending:", nums)

nums.sort(reverse=True)
print("Descending:", nums)


print("Index of 8:", nums.index(8))