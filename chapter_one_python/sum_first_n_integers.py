
# Exercise: Sum of the First n Positive Integers
#
# Write a program that takes a positive integer n as input
# and displays the sum of all integers from 1 to n.
#
# Formula: n * (n + 1) / 2

n = int(input())

total = n * (n + 1) // 2

print(f"The sum of the first {n} positive integers is {total}")