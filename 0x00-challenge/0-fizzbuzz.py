#!/usr/bin/env python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of both three and five print "FizzBuzz".
    - For multiples of three print "Fizz".
    - For multiples of five print "Buzz".
    """
    if n <= 0:
        print("Invalid number. Please provide a positive integer.")
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:  # Check for multiples of both 3 and 5 first
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:  # Check for multiples of 3
            tmp_result.append("Fizz")
        elif (i % 5) == 0:  # Check for multiples of 5
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
