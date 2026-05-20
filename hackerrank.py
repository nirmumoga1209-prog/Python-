def find_max(nums):
    if not nums:
        return None
    maximum = nums[0]
    for value in nums[1:]:
        if value > maximum:
            maximum = value
    return maximum


def find_min(nums):
    if not nums:
        return None
    minimum = nums[0]
    for value in nums[1:]:
        if value < minimum:
            minimum = value
    return minimum


def reverse_list(nums):
    reversed_list = []
    for i in range(len(nums) - 1, -1, -1):
        reversed_list.append(nums[i])
    return reversed_list


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))
    print("Reversed:", reverse_list(numbers))
