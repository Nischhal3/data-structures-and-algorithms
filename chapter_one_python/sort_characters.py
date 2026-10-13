
# Exercise: Sort Characters
#
# Write a program that takes a single string as input
# and sorts its characters from the lowest Unicode value
# to the highest Unicode value. Print the resulting string.
#
# Examples:
# Input:  wikipedia
# Output: adeiiikpw
#
# Input:  assume
# Output: aemssu


# Solution
text = input("Enter a string: ")
print(''.join(sorted(text)))