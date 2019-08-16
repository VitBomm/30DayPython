#Task
# You are given a string S
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

# Input Format
# A single line containing S the string  and integer value k separated by a space.

# Output Format
# Print the combinations with their replacements of string S on separate lines.

from itertools import combinations_with_replacement

S, k = input().split() 

[print(''.join(index)) for index in list(combinations_with_replacement(sorted(S),int(k)))]
