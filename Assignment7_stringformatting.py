"""
Problem Statement :---
Given an integer , print the following values for each integer from 1 to n : Decimal Octal Hexadecimal (capitalized) Binary Function Description Complete the print_formatted function in the editor below. print_formatted has the following parameters: int number: the maximum value to print Prints The four values must be printed on a single line in the order specified above for each from to . Each value should be space-padded to match the width of the binary value of and the values should be separated by a single space.

"""

def print_formatted(number):
    width = len(bin(number)[2:])  # Determine width based on binary representation
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

n = int(input("Enter the maximum value to print: "))
print("Decimal Octal   Hexadecimal Binary")
print_formatted(n)

"""
Sample output :-
Enter the maximum value to print: 8
Decimal Octal   Hexadecimal Binary
   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
"""