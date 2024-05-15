#!/usr/bin/python3
"""
Main file for testing
"""

def minOperations(n):
    if n <= 1:
        return 0
    # Initialize operations count and divisor
    operations = 0
    divisor = 2
    # Factorize n to find the sum of factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

# Example usage:
print("Min # of operations to reach 4 char:", minOperations(4))  # Output: 4
print("Min # of operations to reach 12 char:", minOperations(12)) # Output: 7
