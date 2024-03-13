"""
Problem Statement : -
You are given a 1-D array, . Your task is to print the floor ,ceil  and rint of all the elements of .

Note
In order to get the correct output format, add the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format

A single line of input containing the space separated elements of array A.

Output Format

On the first line, print floor the  of A.
On the second line, print ceil the  of A.
On the third line, print the rint  of A.
"""
"""
Sample Output :-
input:-1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
output:-

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
import numpy as np
np.set_printoptions(legacy='1.13')  # Add this line to get the correct output format
arr = np.array(input().split(), float)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))