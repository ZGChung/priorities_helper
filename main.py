import os

input_path = 'input_list.txt'
# input_path = 'input_list_short.txt'
output_path = 'output_list.txt'

# Read input file
with open(input_path, 'r') as f:
    input_list = f.readlines()

# process the input
# remove trailing '\n'
input_list = [x.strip() for x in input_list]
# remove the '- ' at the beginning for each line
input_list = [x[2:] for x in input_list]

# print(input_list)

# Function to compare two priorities
def compare_priorities(p1, p2):
    print("------------------------------")
    print(f"1: {p1}")
    print(f"2: {p2}")
    choice = input("Which is more important? (1/2): ")
    return p1 if choice == '1' else p2

# Sorting function
def sort_priorities(priorities):
    if len(priorities) <= 1:
        return priorities

    mid = len(priorities) // 2
    left = sort_priorities(priorities[:mid])
    right = sort_priorities(priorities[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare_priorities(left[i], right[j]) == left[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Sort the input list
sorted_list = sort_priorities(input_list)

# Write output file
with open(output_path, 'w') as f:
    for priority in sorted_list:
        f.write(priority + '\n')

print("Sorted priorities have been saved to", output_path)