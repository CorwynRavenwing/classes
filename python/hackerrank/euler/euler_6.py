#!/bin/python3

# import sys

def euler_6(n):
    numbers = range(1, n+1)
    print("#:", list(numbers))
    squares = [
        i * i
        for i in numbers
    ]
    print("#^", squares)
    sum_of_squares = sum(squares)
    total = sum(numbers)
    square_of_sums = total * total
    diff = square_of_sums - sum_of_squares
    print("#SOS", sum_of_squares, square_of_sums, diff)
    return diff

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_6(n))

