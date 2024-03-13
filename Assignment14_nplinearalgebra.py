"""
Problem Statement : -
Task

You are given a square matrix  with dimensions N*N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer .
The next  lines contains the  space separated elements of array .

Output Format

Print the determinant of A .
"""
"""
Sample Output :-
2
1.1 1.1
1.1 1.1
0.00
"""
import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], float)

determinant = np.linalg.det(A)
print("{:.2f}".format(determinant))