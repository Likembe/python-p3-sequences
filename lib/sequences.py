#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []

    if length == 0:
        print(fibonacci_sequence)
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        a, b = 0, 1
        fibonacci_sequence.extend([a, b])

        while len(fibonacci_sequence) < length:
            next_number = a + b
            fibonacci_sequence.append(next_number)
            a, b = b, next_number

        print(fibonacci_sequence)

# Example usage:
print_fibonacci(0)  # Prints an empty list
print_fibonacci(1)  # Prints [0]
print_fibonacci(10)  # Prints [0, 1, 1, 2, 3]
