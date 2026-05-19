# Pattern Compression on a List
# Convert repeated elements into tuple format (element, count)

def compress_pattern(lst):
    """
    Compress a list by converting repeated elements into tuples.
    Example: [1,1,1,2,2,3,3,3] → [(1,3),(2,2),(3,3)]
    """
    
    if not lst:
        return []
    
    compressed = []
    current_element = lst[0]
    count = 1
    
    # Iterate through the list starting from second element
    for i in range(1, len(lst)):
        if lst[i] == current_element:
            # Same element, increment count
            count += 1
        else:
            # Different element, save the tuple and start new count
            compressed.append((current_element, count))
            current_element = lst[i]
            count = 1
    
    # Don't forget the last group
    compressed.append((current_element, count))
    
    return compressed

def display_compression(lst):
    """Display the compression results"""
    compressed = compress_pattern(lst)
    print("=" * 60)
    print("PATTERN COMPRESSION")
    print("=" * 60)
    print(f"Input List:    {lst}")
    print(f"Compressed:    {compressed}")
    print("=" * 60)

# Sample Input from problem
input1 = [1, 1, 1, 2, 2, 3, 3, 3]
display_compression(input1)

# Additional test cases
print("\nAnother Example:")
input2 = [5, 5, 5, 5, 3, 3, 1, 1, 1, 1, 1]
display_compression(input2)

print("\nNo Repeats:")
input3 = [1, 2, 3, 4, 5]
display_compression(input3)

print("\nAll Same Elements:")
input4 = [7, 7, 7, 7, 7]
display_compression(input4)

print("\nSingle Element:")
input5 = [9]
display_compression(input5)

print("\nMixed Pattern:")
input6 = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
display_compression(input6)
