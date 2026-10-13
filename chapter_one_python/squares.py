
# Exercise: Squares
#
# Write a program that prints a dictionary where the keys
# are numbers from 1 to N and the values are the squares of the keys.

n = int(input())

squares = {i: i ** 2 for i in range(1, n + 1)}

print(squares)