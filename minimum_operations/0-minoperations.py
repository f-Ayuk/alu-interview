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


# Testing the function
if __name__ == "__main__":
    n1 = 4
    print(
        "Min number of operations to reach {} characters: {}".format(
            n1, minOperations(n1)))

    n2 = 12
    print(
        "Min number of operations to reach {} characters: {}".format(
            n2, minOperations(n2)))
