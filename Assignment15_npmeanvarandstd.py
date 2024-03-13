"""
Problem Statement : -
Task


You are given a 2-D array of size N * M.
Your task is to find:

The mean along axis 1.
The var along axis  0.
The std along axis None
Input Format

The first line contains the space separated values of N and M.
The next N  lines contains M  space separated integers.

Output Format

First, print the mean.
Second, print the var.
Third, print the std.
"""
"""
Sample Output :-
2 2
1 2
3 4
[1.5 3.5]
[1. 1.]
1.118033988749895

"""
import numpy as np
N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], int)

mean = np.mean(arr, axis=1)
var = np.var(arr, axis=0)
std = np.std(arr)

print(mean)
print(var)
print(std)