"""
Problem Statement : -
Task

You are given a 2-D array with dimensions N*M.
Your task is to perform the min function over axis 1  and then find the max of that.

Input Format

The first line of input contains the space separated values of  N and M.
The next N  lines contains M  space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.
"""
"""
Sample Output :-
Enter two dimentional array as N*M :- 4 2
2 5
2 7
1 3
4 0
2
"""
import numpy as np
N, M = map(int, input(" Enter two dimentional array as N*M :- ").split())
arr = np.array([input().split() for _ in range(N)], int)

result = np.max(np.min(arr, axis=1))
print(result)